# Generated by Django 5.1.2 on 2024-12-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0008_curso_stock_venda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='date',
            new_name='data_venda',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='quantity',
        ),
        migrations.AddField(
            model_name='curso',
            name='estoque',
            field=models.PositiveIntegerField(default=0),
        ),
    ]