# Generated by Django 4.0.4 on 2022-04-19 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_alter_superhero_jenis_kelamin'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='superhero',
            table='hero_superhero',
        ),
    ]
