# Generated by Django 4.2.7 on 2024-04-14 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0016_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='timestamp',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.room'),
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]