# Generated by Django 4.2.11 on 2024-04-21 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_rename_descount_products_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RenameField(
            model_name='products',
            old_name='descriptions',
            new_name='description',
        ),
    ]