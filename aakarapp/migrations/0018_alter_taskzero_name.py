# Generated by Django 4.1 on 2023-10-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aakarapp", "0017_taskzero_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskzero",
            name="name",
            field=models.CharField(
                default="Please update your profile!", max_length=200
            ),
        ),
    ]