# Generated by Django 4.1.5 on 2023-02-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0020_rename_send_order_is_order_send_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(verbose_name='Сумма'),
        ),
    ]
