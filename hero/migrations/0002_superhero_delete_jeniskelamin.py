# Generated by Django 4.0.4 on 2022-04-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Jeniskelamin',
        ),
    ]
