# Generated by Django 4.0.4 on 2022-04-27 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_consaltations_category_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='consult_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.consaltations'),
        ),
    ]
