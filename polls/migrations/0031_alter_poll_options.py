# Generated by Django 3.2.8 on 2021-10-20 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_auto_20211020_0203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'permissions': (('can_data_begin_money', 'Can view data_begin'),)},
        ),
    ]
