# Generated by Django 5.0.3 on 2024-04-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sncfapp', '0004_alter_trains_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='trains',
            name='image',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
