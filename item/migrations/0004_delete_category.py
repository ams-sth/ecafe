# Generated by Django 4.0.5 on 2022-07-25 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
