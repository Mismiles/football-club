# Generated by Django 3.1.1 on 2020-10-01 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_user',
            new_name='user',
        ),
    ]