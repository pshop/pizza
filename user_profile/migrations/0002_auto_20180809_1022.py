# Generated by Django 2.1 on 2018-08-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postaladdress',
            name='postal_code',
            field=models.CharField(max_length=5),
        ),
    ]
