# Generated by Django 5.1 on 2024-11-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exceldata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetalAverageAnnualModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('year', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('value', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'metal_average_annual',
            },
        ),
    ]
