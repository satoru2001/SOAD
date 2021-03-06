# Generated by Django 2.2.16 on 2020-11-26 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apointment_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_id_1', models.CharField(max_length=20)),
                ('date_filed', models.DateField()),
                ('time_filed', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('pa_id', models.CharField(max_length=20)),
                ('age_1', models.CharField(max_length=5)),
                ('doc_name', models.CharField(max_length=30)),
                ('comp', models.CharField(max_length=200)),
                ('medicine', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='media/images/')),
            ],
        ),
    ]
