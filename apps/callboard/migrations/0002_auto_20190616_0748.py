# Generated by Django 2.2.1 on 2019-06-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название категории'),
        ),
    ]
