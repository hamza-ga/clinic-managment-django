# Generated by Django 4.0.4 on 2022-04-25 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_consaltations_x_rays_else'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consaltations',
            name='x_rays_else',
            field=models.ImageField(blank=True, upload_to='consultation_image/<django.db.models.fields.related.ForeignKey>/'),
        ),
    ]
