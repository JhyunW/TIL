# Generated by Django 4.2.2 on 2023-10-19 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='updated_ar',
            new_name='updated_at',
        ),
    ]
