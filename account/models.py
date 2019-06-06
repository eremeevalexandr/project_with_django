from django.db import models

# Таблица с логином и паролем юзера
class Account(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

# Таблица с пресональными данными юзера
class Information(models.Model):
    person = models.OneToOneField(
        Account,
        on_delete = models.CASCADE,
        primary_key = True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

# Таблица со статусами юзера
class Status(models.Model):
    person = models.OneToOneField(
        Account,
        on_delete = models.CASCADE,
        primary_key = True
    )
    email_confirm = models.BooleanField(default = False)