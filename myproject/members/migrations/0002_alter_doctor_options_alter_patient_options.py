# Generated by Django 4.0.4 on 2022-04-23 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'verbose_name': 'doctor', 'verbose_name_plural': 'doctors'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'patient', 'verbose_name_plural': 'patients'},
        ),
    ]
