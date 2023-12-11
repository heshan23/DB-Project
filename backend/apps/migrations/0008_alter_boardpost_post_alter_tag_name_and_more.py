# Generated by Django 4.1.1 on 2023-12-11 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_alter_tagpost_unique_together_alter_boardpost_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardpost',
            name='post',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=8, unique=True, verbose_name='tag_name'),
        ),
        migrations.AlterUniqueTogether(
            name='tagpost',
            unique_together={('tag', 'post')},
        ),
    ]