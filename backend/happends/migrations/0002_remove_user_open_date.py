# Generated by Django 4.1.1 on 2023-11-19 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happends', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='open_date',
        ),
    ]
