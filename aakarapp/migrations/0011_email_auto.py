# Generated by Django 4.1 on 2022-12-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aakarapp', '0010_taskthree'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]