# Generated by Django 5.0.3 on 2024-03-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('trainId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
