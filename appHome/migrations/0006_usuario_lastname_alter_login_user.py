# Generated by Django 5.1.2 on 2024-12-06 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0005_alter_usuario_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='lastname',
            field=models.CharField(default='Sem Sobrenome', max_length=255),
        ),
        migrations.AlterField(
            model_name='login',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appHome.usuario'),
        ),
    ]
