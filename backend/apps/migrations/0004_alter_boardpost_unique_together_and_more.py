# Generated by Django 4.1.1 on 2023-12-05 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_alter_tag_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='boardpost',
            unique_together={('board', 'post')},
        ),
        migrations.AlterUniqueTogether(
            name='tagpost',
            unique_together={('tag', 'post')},
        ),
    ]