# Generated by Django 5.0.1 on 2024-01-10 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='detail',
        ),
    ]
