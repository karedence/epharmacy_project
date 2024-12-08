# Generated by Django 5.1.1 on 2024-12-06 10:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_searchlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchlog',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='searchlog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]