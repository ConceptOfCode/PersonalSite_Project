# Generated by Django 3.1 on 2020-08-31 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalSite_Application', '0003_auto_20200828_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesreceived',
            name='phoneNumberSender',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(13)]),
        ),
    ]
