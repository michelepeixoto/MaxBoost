# Generated by Django 2.0.4 on 2018-07-01 03:03

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180701_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.FileField(default='../media/profile_pics/default_profile_pic.png', storage=django.core.files.storage.FileSystemStorage(location='/Users/mpeixoto/PycharmProjects/MaxBoost/MaxBoost/main/media/'), upload_to='profile_pics'),
        ),
    ]
