# Generated by Django 2.2.5 on 2020-11-12 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0004_auto_20201110_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]
