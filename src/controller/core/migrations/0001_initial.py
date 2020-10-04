# Generated by Django 3.0.8 on 2020-09-10 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=120)),
                ('lastname', models.CharField(blank=True, max_length=120)),
                ('subject', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labname', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=32)),
                ('os', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hostname', models.CharField(blank=True, max_length=120)),
                ('IPAddress', models.GenericIPAddressField(blank=True, null=True)),
                ('OS', models.CharField(blank=True, max_length=32)),
                ('status', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('output', models.TextField(blank=True)),
                ('Lastcommand', models.CharField(blank=True, max_length=120)),
                ('runcommand', models.BooleanField(default=False)),
                ('lab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Lab')),
            ],
        ),
    ]