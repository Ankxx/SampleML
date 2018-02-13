# Generated by Django 2.0.2 on 2018-02-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predict',
            name='destLocation',
        ),
        migrations.AddField(
            model_name='predict',
            name='destinationLocation',
            field=models.CharField(default='NaN', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='predict',
            name='originLocation',
            field=models.CharField(max_length=200),
        ),
    ]