# Generated by Django 5.1.2 on 2024-11-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Play_App', '0008_word_is_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='lock_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='زمان قفل شدن بازی'),
        ),
    ]