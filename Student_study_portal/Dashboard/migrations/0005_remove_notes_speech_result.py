# Generated by Django 4.2.7 on 2023-12-22 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0004_rename_assignments_assignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='speech_result',
        ),
    ]