# Generated by Django 3.2.19 on 2023-08-21 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retro', '0045_alter_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comment_title', to='retro.article'),
        ),
    ]
