from django.db import models
# Example app name is myapp


class ChoiceType(models.Model):
    name = models.CharField(max_length=50)


class Widget(models.Model):
    name = models.CharField(max_length=50)
    field1 = models.CharField(max_length=50)
    field2 = models.CharField(max_length=50)
    choice = models.ForeignKey(ChoiceType)


class Thing(models.Model):
    name = models.CharField(max_length=50)
