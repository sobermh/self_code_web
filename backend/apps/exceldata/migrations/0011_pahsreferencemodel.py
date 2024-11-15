# Generated by Django 5.1 on 2024-11-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exceldata', '0010_landuseratiomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PAHsReferenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('year', models.IntegerField(null=True)),
                ('reference_number', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'PAHs_reference',
            },
        ),
    ]
