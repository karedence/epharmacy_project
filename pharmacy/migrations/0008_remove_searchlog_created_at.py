# Generated by Django 5.1.1 on 2024-12-06 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0007_remove_searchlog_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchlog',
            name='created_at',
        ),
    ]
