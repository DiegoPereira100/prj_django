# Generated by Django 5.1.2 on 2024-12-06 13:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0007_remove_usuario_email_alter_login_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appHome.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appHome.usuario')),
            ],
        ),
    ]
