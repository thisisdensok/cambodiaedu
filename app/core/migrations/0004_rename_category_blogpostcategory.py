# Generated by Django 5.0.1 on 2024-02-27 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_post_body_english_remove_post_body_khmer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='BlogPostCategory',
        ),
    ]
