# Generated by Django 3.2.18 on 2023-04-29 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_staff_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, max_length=10),
        ),
    ]
