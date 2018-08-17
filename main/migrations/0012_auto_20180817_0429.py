# Generated by Django 2.0.4 on 2018-08-17 04:29

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180807_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.FileField(default='settings.MEDIA_ROOT/profile_pics/default_profile_pic.png', storage=django.core.files.storage.FileSystemStorage(location='/Users/mpeixoto/PycharmProjects/MaxBoost/main/media/'), upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'required': 'Required field'}, max_length=22, verbose_name='username'),
        ),
    ]
