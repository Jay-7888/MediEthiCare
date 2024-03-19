# Generated by Django 5.0.1 on 2024-02-09 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0017_hospital_hospital_doc'),
        ('userapp', '0011_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalapp.medicine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.user')),
            ],
        ),
    ]