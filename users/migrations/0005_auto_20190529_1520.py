# Generated by Django 2.2.1 on 2019-05-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190529_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='arriving_time',
            field=models.DateTimeField(verbose_name='arriving time'),
        ),
    ]
