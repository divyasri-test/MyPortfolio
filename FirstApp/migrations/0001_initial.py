# Generated by Django 3.2.15 on 2023-07-31 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]
