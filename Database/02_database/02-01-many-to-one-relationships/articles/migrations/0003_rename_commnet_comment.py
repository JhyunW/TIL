# Generated by Django 4.2.5 on 2023-10-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_commnet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='commnet',
            new_name='Comment',
        ),
    ]
