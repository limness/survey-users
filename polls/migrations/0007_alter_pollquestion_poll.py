# Generated by Django 3.2.8 on 2021-10-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_pollquestion_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollquestion',
            name='poll',
            field=models.CharField(default='', max_length=200),
        ),
    ]
