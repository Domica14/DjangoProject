# Generated by Django 5.1.7 on 2025-03-07 00:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'user_auth',
            },
        ),
    ]
