# Generated by Django 5.0.7 on 2024-08-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='conversion_rate',
            field=models.FloatField(default=80),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
