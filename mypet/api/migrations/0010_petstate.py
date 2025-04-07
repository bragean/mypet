# Generated by Django 5.0.9 on 2025-04-07 02:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_point_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('created_by', models.UUIDField(editable=False, null=True)),
                ('modified_by', models.UUIDField(editable=False, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('color', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20, unique=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
