# Generated by Django 3.2.9 on 2021-11-27 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_core_user_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core_user',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]