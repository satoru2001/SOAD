# Generated by Django 2.2.16 on 2020-11-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_page', '0004_auto_20201119_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='docname',
            field=models.CharField(default='Himangshu', max_length=100),
        ),
        migrations.AddField(
            model_name='doc',
            name='hospital',
            field=models.CharField(default='SunRise', max_length=100),
        ),
    ]
