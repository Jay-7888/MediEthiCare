# Generated by Django 5.0.1 on 2024-02-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_alter_hospital_otp_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='otp',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='otp_status',
            field=models.CharField(default='Not Verified', max_length=15),
        ),
    ]
