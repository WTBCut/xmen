# Generated by Django 4.0.4 on 2022-04-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jeniskelamin',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('jenis', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'jeniskelamin',
            },
        ),
    ]