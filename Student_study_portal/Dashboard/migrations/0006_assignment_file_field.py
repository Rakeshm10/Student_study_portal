# Generated by Django 4.2.7 on 2024-01-19 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_remove_notes_speech_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='file_field',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]