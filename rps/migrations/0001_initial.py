# Generated by Django 2.2 on 2020-02-16 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noKTP', models.IntegerField()),
                ('nama', models.CharField(max_length=50)),
                ('tanggalLahir', models.DateField()),
                ('jenisKelamin', models.CharField(max_length=10)),
                ('agama', models.CharField(choices=[('islam', 'Islam'), ('katolik', 'Katolik'), ('kristen', 'Kristen'), ('hindu', 'Hindu'), ('budha', 'Budha'), ('konghucu', 'Konghucu')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
