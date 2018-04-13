from database_helper import DatabaseHelper


class MyDBH(DatabaseHelper):
    widget = ('myapp', 'Widget')
    thing = ('myapp', 'Thing')

    def get_widget(self, name):
        return self.get_object(*self.widget, name=name)

    def create_widget(self, name, field1, field2, choice):
        kwargs = {'name': name, 'field1': field1,
                  'field2': field2, 'choice': choice}
        return self.create_object(*self.widget, **kwargs)

    def get_thing(self, name):
        return self.get_object(*self.thing, name=name)

