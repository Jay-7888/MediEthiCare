# Generated by Django 5.0.1 on 2024-02-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_appointment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]