# Generated by Django 5.1 on 2024-09-20 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_hallbooking_rename_adminsettings_adminsetting_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriestProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('role', models.CharField(blank=True, max_length=10, null=True)),
                ('firstname', models.CharField(max_length=50)),
                ('othernames', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(max_length=11)),
                ('phone', models.CharField(max_length=11)),
                ('position', models.CharField(max_length=50)),
                ('date_of_birth', models.DateTimeField()),
                ('photo', models.ImageField(upload_to='')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
            options={
                'db_table': 'priest_profile',
            },
        ),
    ]
