# Generated by Django 3.0.14 on 2022-02-12 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('mrp', models.FloatField()),
                ('warranty', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('maxqty', models.IntegerField()),
                ('brand', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='headset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('mrp', models.FloatField()),
                ('warranty', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('maxqty', models.IntegerField()),
                ('brand', models.CharField(max_length=255)),
                ('headsettype', models.CharField(max_length=255)),
            ],
        ),
    ]
