# Generated by Django 5.1.2 on 2024-11-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0004_alter_myuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
