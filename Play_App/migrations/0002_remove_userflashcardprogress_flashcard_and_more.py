# Generated by Django 5.1.2 on 2024-11-03 14:34

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Play_App', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userflashcardprogress',
            name='flashcard',
        ),
        migrations.RemoveField(
            model_name='userflashcardprogress',
            name='user',
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_word', models.CharField(max_length=255, verbose_name='Front Word')),
                ('back_word', models.CharField(max_length=255, verbose_name='Back Word')),
                ('box', models.IntegerField(default=1)),
                ('current_day', models.IntegerField(default=1)),
                ('last_reviewed', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Flashcard',
        ),
        migrations.DeleteModel(
            name='UserFlashcardProgress',
        ),
    ]
