# Generated by Django 4.1.6 on 2023-02-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0004_apiauthkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiauthkey',
            name='auth_key',
            field=models.CharField(db_index=True, max_length=250, unique=True),
        ),
    ]
