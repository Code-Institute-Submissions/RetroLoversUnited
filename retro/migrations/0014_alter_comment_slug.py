# Generated by Django 3.2.19 on 2023-06-26 19:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retro', '0013_profile_computer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
