# Generated by Django 3.0.2 on 2020-02-02 17:59

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
