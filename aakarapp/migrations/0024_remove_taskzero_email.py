# Generated by Django 4.1 on 2023-10-27 19:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("aakarapp", "0023_taskzero_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="taskzero",
            name="email",
        ),
    ]
