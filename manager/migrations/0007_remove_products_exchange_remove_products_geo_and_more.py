# Generated by Django 4.2.1 on 2023-05-07 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_alter_clients_options_alter_exchanges_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='exchange',
        ),
        migrations.RemoveField(
            model_name='products',
            name='geo',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='products',
            name='resident',
        ),
    ]