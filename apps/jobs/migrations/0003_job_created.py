# Generated by Django 3.2.6 on 2022-07-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
