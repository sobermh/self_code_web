# Generated by Django 5.1 on 2024-11-06 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exceldata', '0011_pahsreferencemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pahscancerriskmodel',
            name='factor',
        ),
    ]
