# Generated by Django 4.0.5 on 2022-07-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('phonenumber', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
