# Generated by Django 2.2 on 2020-02-28 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olahDataRPS', '0010_auto_20200227_1556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rps',
            options={'ordering': ['-id'], 'verbose_name': 'rps', 'verbose_name_plural': 'rps'},
        ),
    ]
