# Generated by Django 4.2 on 2023-05-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_alter_enseignant_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignant',
            name='photo',
            field=models.ImageField(default='prof/img/pdp/23/user.png', upload_to='prof/img/pdp/%y'),
        ),
    ]
