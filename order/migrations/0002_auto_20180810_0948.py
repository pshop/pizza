# Generated by Django 2.1 on 2018-08-10 09:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20180809_1239'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0006_menu'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 8, 10, 9, 48, 56, 788534, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_by_card', models.BooleanField()),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 8, 10, 9, 48, 56, 787797, tzinfo=utc))),
                ('card_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.CardPayment')),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.PostalAddress')),
                ('invoice_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Invoices', to='user_profile.PostalAddress')),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Panier')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.ManyToManyField(related_name='Invoices', through='order.History', to='order.Status'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='history',
            name='Invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Invoice'),
        ),
        migrations.AddField(
            model_name='history',
            name='Status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Status'),
        ),
    ]