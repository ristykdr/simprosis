# Generated by Django 2.2 on 2020-02-29 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rps', '0006_auto_20200220_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='fakultas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaFakultas', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'fakultas',
                'verbose_name_plural': 'fakultass',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='prodi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaProdi', models.CharField(max_length=50)),
                ('fak', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rps.fakultas')),
            ],
            options={
                'verbose_name': 'prodi',
                'verbose_name_plural': 'prodis',
                'ordering': ['-id'],
            },
        ),
    ]
