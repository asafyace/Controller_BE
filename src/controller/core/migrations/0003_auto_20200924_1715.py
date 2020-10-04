# Generated by Django 3.0.8 on 2020-09-24 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_command'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='os',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='server',
            name='timestamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
