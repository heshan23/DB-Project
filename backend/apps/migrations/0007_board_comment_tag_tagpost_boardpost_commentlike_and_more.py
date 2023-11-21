# Generated by Django 4.1.1 on 2023-11-21 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_postlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='board_name')),
            ],
            options={
                'verbose_name': 'board',
                'db_table': 'board',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='text')),
                ('res_comment', models.IntegerField(default=-1, verbose_name='res_to_comment_id')),
                ('create_date', models.DateField(verbose_name='create_date')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.post', verbose_name='post_id')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.user', verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'comment',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name='tag_name')),
            ],
            options={
                'verbose_name': 'tag',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.post', verbose_name='post')),
                ('tag', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.tag', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'tag_post',
                'db_table': 'tags_post',
            },
        ),
        migrations.CreateModel(
            name='BoardPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.board', verbose_name='board')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.post', verbose_name='post')),
            ],
            options={
                'verbose_name': 'board_post',
                'db_table': 'board_post',
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.comment', verbose_name='comment_id')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.user', verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'like_comment',
                'db_table': 'likes_comment',
                'unique_together': {('user', 'comment')},
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.post', verbose_name='post_id')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.user', verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'collection',
                'db_table': 'collection',
                'unique_together': {('user', 'post')},
            },
        ),
    ]
