# Generated by Django 3.2 on 2023-01-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_order',
            field=models.PositiveIntegerField(),
        ),
    ]
