# Generated by Django 5.1 on 2024-11-05 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exceldata', '0003_metalreferencemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialeconomymodel',
            name='province',
        ),
    ]
