# Generated by Django 4.1 on 2022-08-31 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('link', models.CharField(max_length=1000)),
                ('short_link', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
