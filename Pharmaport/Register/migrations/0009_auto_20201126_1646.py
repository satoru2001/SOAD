# Generated by Django 2.2.16 on 2020-11-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0008_auto_20201126_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='doctor_id',
            field=models.CharField(default='Not doctor', max_length=12, null=True),
        ),
    ]