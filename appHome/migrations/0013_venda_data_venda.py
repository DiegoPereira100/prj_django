# Generated by Django 5.1.2 on 2024-12-06 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0012_remove_venda_data_compra_alter_venda_quantidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data_venda',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
