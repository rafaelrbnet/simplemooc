# Generated by Django 2.0.6 on 2018-07-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20180705_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='embedded',
            field=models.TextField(blank=True, verbose_name='Vídeo Externo'),
        ),
    ]
