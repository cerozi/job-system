# Generated by Django 3.2.6 on 2022-07-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220701_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='scholarship',
            field=models.CharField(choices=[('0', 'Ensino Fundamental'), ('1', 'Ensino Médio'), ('2', 'Tecnólogo'), ('3', 'Ensino Superior'), ('4', 'Mestrado'), ('5', 'Doutorado')], max_length=1, null=True),
        ),
    ]