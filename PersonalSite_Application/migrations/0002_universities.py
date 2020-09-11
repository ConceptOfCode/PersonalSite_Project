# Generated by Django 3.1 on 2020-08-28 10:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalSite_Application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniName', models.CharField(max_length=50)),
                ('uniDescriptions', models.CharField(max_length=100)),
                ('uniEnterDate', models.CharField(max_length=12, null=True)),
                ('uniYearsEducation', models.PositiveIntegerField(verbose_name=django.core.validators.MaxLengthValidator(2))),
                ('uniDegree', models.CharField(max_length=50, null=True)),
                ('uniMajor', models.CharField(max_length=50, null=True)),
                ('uniCity', models.CharField(max_length=50, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PersonalSite_Application.profile')),
            ],
        ),
    ]
