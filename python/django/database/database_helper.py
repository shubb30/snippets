from django.apps import apps
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def is_string(string):
    return isinstance(string, str) or isinstance(string, unicode)


def get_model_dec(func):
    """ Decorator that checks if the model passed to the
        function is a string or a model class.
        Sets the model to the model object if a string
        is passed.
    """
    def wrapper(self, app_name, model, *args, **kwargs):
        if is_string(model):
            model = self._get_model(app_name, model)
        return func(self, app_name, model, *args, **kwargs)
    return wrapper


def get_model(app_name, model_name):
    """ Get a model Class.

    @params
        app_name: Name of the Django app
        model_name: Name of the model
    @returns
        Django model class object

    """
    return apps.get_model(app_label=app_name.lower(), model_name=model_name)


class DatabaseHelper(object):
    """ Helper class to create Django QuerySets and objects.
        Allows user to specify models by string or by model Class.
        Has shortcuts to fetch other common Django objects such as
        User, and ContentType.
    """
    def __init__(self):
        self._models = {}
        self._content_types = {}
        self.cache = LazyCache()

    def _get_model(self, app_name, model_name):
        """ Get the model class, and cache it.

        @params:
            app_name: Name of the Django app
            model_name: Name of the model
        @returns:
            The model class if it exists.
            None if the model does not exist.
        """
        key = "{}:{}".format(app_name, model_name)
        if not self._models.get(key):
            try:
                self._models[key] = get_model(app_name, model_name)
            except LookupError:
                return None
        return self._models[key]

    def get_user_object(self, **kwargs):
        """ Retrieves a User object.

        @params
            kwargs - keyword arguments to query for (username,
                     first_name, last_name, email.
        @returns
            User object if found matching kwargs
            None if no user is found.
        """
        return self.get_object_or_none(None, User, **kwargs)

    @get_model_dec
    def get_object(self, app_name, model, **kwargs):
        """ Fetch a Django database model instance.

        @params>
            app_name: Name of the Django app
            model_name: Name of the model
            kwargs: keyword arguments to query
        @returns:
            Result of the Django query
        """
        return model.objects.get(**kwargs)

    @get_model_dec
    def get_object_or_none(self, app_name, model, **kwargs):
        """ Fetch a Django database model instance if it exists.

        @params>
            app_name: Name of the Django app
            model_name: Name of the model
            kwargs: keyword arguments to query
        @returns:
            Result of the Django query
            None if the result is not found
        """
        try:
            return self.get_object(app_name, model, **kwargs)
        except model.DoesNotExist:
            print "cannot find {} object using kwargs {}".format(model, kwargs)
            return None

    @get_model_dec
    def get_qs(self, app_name, model, **kwargs):
        """ Fetch a Django database Queryset.

        @params>
            app_name: Name of the Django app
            model_name: Name of the model
            kwargs: keyword arguments to query
        @returns:
            Queryset of kwargs
        """
        return model.objects.filter(**kwargs)

    @get_model_dec
    def create_object(self, app_name, model, **kwargs):
        """ Create a Django database entry.

        @params>
            app_name: Name of the Django app
            model_name: Name of the model
            kwargs: keyword arguments insert
        @returns:
            Django object that was created.
        """
        return model.objects.create(**kwargs)

    @get_model_dec
    def get_or_create(self, app_name, model, defaults=None, **kwargs):
        """ Create a Django database entry if it does not exist.

        @params>
            app_name: Name of the Django app
            model_name: Name of the model
            defaults: dictionary of keyword arguments to search for
            kwargs: keyword arguments insert
        @returns:
            Django object that was created if it did not already exist.
            Existing object if it already existed.
        """
        if defaults is None:
            defaults = kwargs
        return model.objects.get_or_create(defaults=defaults, **kwargs)

    def get_user_group(self, group_name):
        """ Fetch a Django user group.

        @params>
            group_name: Name of the user group
        @returns:
            Django user group
            Raises DoesNotExist if group name not found
        """
        kwargs = {'name':group_name}
        return self.get_object(None, Group, **kwargs)

    def get_or_create_user_group(self, group_name):
        """ Fetch a Django user group, creating if doesn't exist

        @params>
            group_name: Name of the user group
        @returns:
            Django user group
        """
        kwargs = {'name':group_name}
        return self.get_or_create(None, Group, defaults=kwargs, **kwargs)[0]

    def get_or_create_permission(self, permission_name, content_type=None, name=None):
        """ Fetch a Django permission object, creating if doesn't exist

        @params>
            permission_name: Short name of the permission (undercores, no spaces)
            content_type: Django content type for the permission
            name: Human readable name of permission (for Django Admin)
        @returns:
            Django user group
        """
        kwargs = {'codename':permission_name}
        defaults = kwargs
        if content_type is not None:
            defaults['content_type'] = content_type
        if name is not None:
            defaults['name'] = name
        return self.get_or_create(None, Permission, defaults=defaults, **kwargs)[0]

    def get_content_type(self, app_name, model_name):
        """ Fetch a Django content type for the model, save to cache

        @params>
            app_name: Name of the Django app
            model_name: Name of the model
        @returns:
            Django content type object
        """
        key = "{}:{}".format(app_name, model_name)
        if not self._content_types.get(key):
            model = self._get_model(app_name, model_name)
            self._content_types[key] = ContentType.objects.get_for_model(model)
        return self._content_types[key]


class LazyCache(object):
    """ Create a cache of objects that will be fetched when they are accessed,
        not when they are instantiated.
        Useful for populating form dropdowns or default values in ModelForms.
    """
    def __init__(self):
        self._cache = {}

    def add(self, key, app_name, model_name, **kwargs):
        """ Add an item to the cache.

        """
        self._cache[key] = {'value': None,
                            'app_name': app_name,
                            'model_name': model_name,
                            'kwargs': kwargs}

    def __getattr__(self, name):
        """ If not already fetched, fetch the QuerySet
            when the attribute is called, and save it to
            the cache.
        @returns
            QuerySet if results is more than 1
            Model object if results is 1
        """
        if name in self._cache:
            if self._cache[name]['value'] is None:
                model = get_model(self._cache[name]['app_name'],
                                  self._cache[name]['model_name'])
                results = model.objects.filter(**self._cache[name]['kwargs'])
                if len(results) == 1:
                    self._cache[name]['value'] = results[0]
                else:
                    self._cache[name]['value'] = results
            return self._cache[name]['value']
        raise AttributeError("object has no attribute '{}'".format(name))
