# Generated by Django 5.0.6 on 2025-02-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canteenvendor',
            name='mobile_number',
            field=models.CharField(max_length=100),
        ),
    ]
