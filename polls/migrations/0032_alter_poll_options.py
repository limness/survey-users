# Generated by Django 3.2.8 on 2021-10-20 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_alter_poll_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'permissions': (('readonly_poll', 'Readonly Poll'),)},
        ),
    ]
