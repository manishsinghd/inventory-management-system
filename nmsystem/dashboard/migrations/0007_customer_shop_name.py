# Generated by Django 3.1.3 on 2020-11-09 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='shop_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
