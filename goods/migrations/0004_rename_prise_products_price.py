# Generated by Django 4.2.11 on 2024-04-16 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_alter_products_descount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='prise',
            new_name='price',
        ),
    ]
