# Generated by Django 2.0.4 on 2018-07-01 02:54

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180701_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.FileField(default='settings.MEDIA_ROOT/profile_pics/default_profile_pic.png', storage=django.core.files.storage.FileSystemStorage(location='/Users/mpeixoto/PycharmProjects/MaxBoost/main/media/'), upload_to='profile_pics'),
        ),
    ]