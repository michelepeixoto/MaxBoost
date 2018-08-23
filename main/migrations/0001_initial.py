# Generated by Django 2.0.4 on 2018-06-29 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=22)),
                ('password', models.CharField(max_length=44)),
                ('email', models.EmailField(max_length=254)),
                ('games_played', models.CharField(max_length=500)),
                ('is_online', models.BooleanField()),
                ('hire_price', models.FloatField()),
                ('time_online', models.FloatField()),
                ('picture', models.FileField(upload_to='')),
            ],
        ),
    ]