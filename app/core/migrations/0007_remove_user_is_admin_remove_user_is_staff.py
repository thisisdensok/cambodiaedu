# Generated by Django 5.0.1 on 2024-03-07 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]