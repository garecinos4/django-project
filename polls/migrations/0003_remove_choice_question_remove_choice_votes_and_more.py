# Generated by Django 5.1.5 on 2025-01-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choicequestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AddField(
            model_name='choicequestion',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
