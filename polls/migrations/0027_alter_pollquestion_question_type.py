# Generated by Django 3.2.8 on 2021-10-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_alter_pollquestion_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollquestion',
            name='question_type',
            field=models.CharField(blank=True, choices=[('own_asnwer', 'own_asnwer'), ('choices_answer', 'choices_answer')], default='own_asnwer', max_length=30),
        ),
    ]
