# Generated by Django 4.0 on 2023-01-29 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_order']},
        ),
    ]
