# Generated by Django 4.1.4 on 2023-01-24 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_appointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='appointment',
        ),
    ]