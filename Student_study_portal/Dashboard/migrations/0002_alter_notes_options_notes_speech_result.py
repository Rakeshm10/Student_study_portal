# Generated by Django 4.2.7 on 2023-12-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'notes', 'verbose_name_plural': 'notes'},
        ),
        migrations.AddField(
            model_name='notes',
            name='speech_result',
            field=models.TextField(blank=True, null=True),
        ),
    ]
