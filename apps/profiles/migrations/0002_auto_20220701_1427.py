# Generated by Django 3.2.6 on 2022-07-01 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Company'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Employee'},
        ),
    ]
