# Generated by Django 4.1.1 on 2023-12-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_notice_isunread_notice_related_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ann',
            name='create_date',
            field=models.DateTimeField(verbose_name='create_date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(verbose_name='create_date'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='create_date',
            field=models.DateTimeField(verbose_name='create_date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(verbose_name='created_date'),
        ),
    ]
