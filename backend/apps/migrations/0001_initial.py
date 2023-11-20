# Generated by Django 4.1.1 on 2023-11-20 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10, verbose_name='user_name')),
                ('email', models.CharField(max_length=127, verbose_name='email')),
                ('password', models.CharField(max_length=10, verbose_name='password')),
                ('avatar', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('content', models.TextField(verbose_name='text')),
                ('create_date', models.DateField(verbose_name='created_date')),
                ('user_name', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='apps.user', verbose_name='user_poster_name')),
            ],
            options={
                'verbose_name': 'post',
                'db_table': 'posts',
            },
        ),
    ]
