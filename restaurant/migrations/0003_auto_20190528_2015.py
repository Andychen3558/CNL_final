# Generated by Django 2.2.1 on 2019-05-28 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20190527_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='eat_time',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='seat_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='skip_probability',
            field=models.FloatField(default=0.1),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='timeout',
            field=models.DurationField(default=datetime.timedelta(seconds=180)),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='waiting_phonenumber',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='waiting_queue',
            field=models.TextField(default=''),
        ),
    ]
