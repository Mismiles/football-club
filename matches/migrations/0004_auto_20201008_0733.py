# Generated by Django 3.1.1 on 2020-10-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20201008_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postm',
            name='man_of_the_match',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
