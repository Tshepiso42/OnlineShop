# Generated by Django 3.1.6 on 2021-02-25 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210212_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Additional_info',
            new_name='additional_info',
        ),
    ]
