# Generated by Django 5.0.9 on 2025-03-18 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(default='f5119806-be7a-4487-bb1a-72db5c26fb25', on_delete=django.db.models.deletion.CASCADE, to='api.post'),
            preserve_default=False,
        ),
    ]
