# Generated by Django 2.2 on 2020-03-11 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olahDataJurnalKuliah', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurnalkuliah',
            name='tahunAjaran',
            field=models.CharField(choices=[(2019, 2019), (2020, 2020)], max_length=10),
        ),
    ]
