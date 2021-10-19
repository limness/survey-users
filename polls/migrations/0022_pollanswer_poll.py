# Generated by Django 3.2.8 on 2021-10-19 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_remove_pollanswer_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollanswer',
            name='poll',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.poll'),
        ),
    ]