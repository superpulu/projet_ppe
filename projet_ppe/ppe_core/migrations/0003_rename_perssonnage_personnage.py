# Generated by Django 5.0 on 2023-12-04 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ppe_core', '0002_perssonnage_name_perssonnage_skin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perssonnage',
            new_name='Personnage',
        ),
    ]
