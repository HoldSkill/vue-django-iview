# Generated by Django 2.1.2 on 2018-10-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xyuser',
            name='avatar',
            field=models.ImageField(blank=True, max_length=10, null=True, upload_to='driver/%Y/%m/%d', verbose_name='头像'),
        ),
    ]
