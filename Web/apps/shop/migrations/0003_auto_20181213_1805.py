# Generated by Django 2.1.2 on 2018-12-13 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181213_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examinestockrecord',
            old_name='stock_in_status',
            new_name='stock_status',
        ),
        migrations.RenameField(
            model_name='examinestockrecord',
            old_name='stock_in_time',
            new_name='stock_time',
        ),
    ]