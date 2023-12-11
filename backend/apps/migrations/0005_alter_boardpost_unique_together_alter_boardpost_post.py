# Generated by Django 4.1.1 on 2023-12-05 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_boardpost_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='boardpost',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='boardpost',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.post', unique=True, verbose_name='post'),
        ),
    ]
