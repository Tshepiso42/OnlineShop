# Generated by Django 3.1.6 on 2021-02-25 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210225_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
    ]
