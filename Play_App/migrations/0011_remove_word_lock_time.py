# Generated by Django 5.1.2 on 2024-11-14 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Play_App', '0010_alter_word_last_reviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='lock_time',
        ),
    ]