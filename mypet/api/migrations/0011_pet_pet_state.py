# Generated by Django 5.0.9 on 2025-04-07 02:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_petstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_state',
            field=models.ForeignKey(default='839fc2dc-d2b5-4dd4-a554-0932831c7998', on_delete=django.db.models.deletion.CASCADE, to='api.petstate'),
            preserve_default=False,
        ),
    ]
