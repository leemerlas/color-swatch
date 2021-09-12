# Generated by Django 3.2.7 on 2021-09-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HSLSwatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swatch_type', models.CharField(max_length=10)),
                ('hue', models.CharField(max_length=10)),
                ('saturation', models.CharField(max_length=10)),
                ('lightness', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RGBSwatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swatch_type', models.CharField(max_length=10)),
            ],
        ),
    ]