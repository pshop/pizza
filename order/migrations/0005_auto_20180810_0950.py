# Generated by Django 2.1 on 2018-08-10 09:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20180810_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 9, 50, 56, 500247, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 10, 9, 50, 56, 499520, tzinfo=utc)),
        ),
    ]