# Generated by Django 2.2.1 on 2019-06-16 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0003_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя объявления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callboard.Category', verbose_name='Категория')),
            ],
        ),
    ]
