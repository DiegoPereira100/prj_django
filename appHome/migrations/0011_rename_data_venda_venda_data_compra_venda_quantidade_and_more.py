# Generated by Django 5.1.2 on 2024-12-06 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0010_rename_estoque_curso_stock'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='data_venda',
            new_name='data_compra',
        ),
        migrations.AddField(
            model_name='venda',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='venda',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
