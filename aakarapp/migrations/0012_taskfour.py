# Generated by Django 4.1 on 2022-12-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aakarapp', '0011_email_auto'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crid', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('marks', models.CharField(max_length=100)),
            ],
        ),
    ]
