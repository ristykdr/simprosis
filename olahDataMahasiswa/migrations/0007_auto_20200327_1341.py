# Generated by Django 2.2 on 2020-03-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olahDataMahasiswa', '0006_remove_mahasiswa_nik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='tahunMasuk',
            field=models.IntegerField(blank=True, choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], null=True),
        ),
    ]
