# Generated by Django 2.2.4 on 2019-08-16 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'pub_date', 'ordering': ['-pub_date', 'title'], 'permissions': (('view_future_post', 'Can view unpublished Post'),), 'verbose_name': 'blog post'},
        ),
    ]
