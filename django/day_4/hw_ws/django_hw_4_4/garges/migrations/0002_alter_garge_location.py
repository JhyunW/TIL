# Generated by Django 4.2.5 on 2023-09-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garge',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
