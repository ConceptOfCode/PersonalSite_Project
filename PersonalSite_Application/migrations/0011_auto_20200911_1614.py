# Generated by Django 3.0.8 on 2020-09-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalSite_Application', '0010_auto_20200909_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='aboutFullText',
            field=models.CharField(max_length=2000),
        ),
    ]
