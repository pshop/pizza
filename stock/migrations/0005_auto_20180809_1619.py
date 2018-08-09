# Generated by Django 2.1 on 2018-08-09 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20180809_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('picture', models.ImageField(upload_to='photos/')),
                ('nb_sold', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unit', models.CharField(max_length=50)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Ingredient')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(related_name='pizzas', through='stock.Recipe', to='stock.Ingredient'),
        ),
    ]