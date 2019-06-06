from django.db import models

class Person(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

class Person_information(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete = models.CASCADE,
        primary_key = True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)