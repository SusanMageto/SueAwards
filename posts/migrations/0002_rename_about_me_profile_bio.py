# Generated by Django 4.0.5 on 2022-06-11 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='about_me',
            new_name='bio',
        ),
    ]
