# Generated by Django 5.0.3 on 2024-04-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sncfapp', '0005_trains_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
