# Generated by Django 2.2.16 on 2020-11-12 14:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users_page', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fies',
            new_name='files',
        ),
    ]
