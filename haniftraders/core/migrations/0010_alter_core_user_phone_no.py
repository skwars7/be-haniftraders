# Generated by Django 3.2.9 on 2021-11-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_core_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core_user',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
