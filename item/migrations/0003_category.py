# Generated by Django 4.0.5 on 2022-07-24 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_remove_item_price_remove_item_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
    ]