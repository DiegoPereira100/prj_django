# Generated by Django 5.1.2 on 2024-11-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0002_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
