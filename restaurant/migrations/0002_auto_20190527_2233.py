# Generated by Django 2.2.1 on 2019-05-27 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='name',
            new_name='restaurant_name',
        ),
    ]
