# Generated by Django 4.1.4 on 2023-01-27 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_appointment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='hospital_profile',
        ),
    ]