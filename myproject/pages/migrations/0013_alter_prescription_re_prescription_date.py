# Generated by Django 4.0.4 on 2022-04-27 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_prescription_re_prescription_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='re_prescription_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
