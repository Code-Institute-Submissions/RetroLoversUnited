# Generated by Django 3.2.19 on 2023-08-21 20:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retro', '0048_comment_comment_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_title',
        ),
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='article.title', unique=True),
        ),
    ]
