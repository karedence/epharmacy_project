# Generated by Django 5.1.1 on 2024-12-06 13:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0008_remove_searchlog_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchlog',
            name='patient',
        ),
        migrations.AddField(
            model_name='searchlog',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
