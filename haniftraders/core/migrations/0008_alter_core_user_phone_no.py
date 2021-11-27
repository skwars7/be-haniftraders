# Generated by Django 3.2.9 on 2021-11-27 04:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211127_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core_user',
            name='phone_no',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
