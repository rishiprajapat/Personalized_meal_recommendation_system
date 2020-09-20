# Generated by Django 3.0.4 on 2020-03-15 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=80)),
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
