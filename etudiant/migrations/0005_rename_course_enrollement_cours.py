# Generated by Django 4.2 on 2023-05-05 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0004_enrollement_datecreation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollement',
            old_name='course',
            new_name='cours',
        ),
    ]