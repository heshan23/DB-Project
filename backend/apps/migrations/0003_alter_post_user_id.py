# Generated by Django 4.1.1 on 2023-11-20 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_post_user_name_post_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.user', verbose_name='user_poster_id'),
        ),
    ]