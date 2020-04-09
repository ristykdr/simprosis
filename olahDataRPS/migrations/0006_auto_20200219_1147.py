# Generated by Django 2.2 on 2020-02-19 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olahDataRPS', '0005_auto_20200219_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referensi',
            name='tahun',
            field=models.SmallIntegerField(max_length=4),
        ),
        migrations.AlterField(
            model_name='rps',
            name='prasyarat',
            field=models.TextField(choices=[('SIM3707', 'Data Mining'), ('SIM3201', 'Logika dan Algoritma'), ('cobakode', 'coba')]),
        ),
    ]
