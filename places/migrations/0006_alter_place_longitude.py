# Generated by Django 3.2.16 on 2023-01-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20230122_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]