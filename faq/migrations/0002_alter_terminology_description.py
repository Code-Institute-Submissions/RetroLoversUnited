# Generated by Django 3.2.19 on 2023-07-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminology',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]