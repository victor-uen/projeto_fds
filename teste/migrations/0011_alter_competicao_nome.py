# Generated by Django 5.1.6 on 2025-04-28 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0010_alter_convite_enviado_por'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicao',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
