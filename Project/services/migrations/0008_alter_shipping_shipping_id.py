# Generated by Django 4.1.4 on 2022-12-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_shipping_shipping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='Shipping_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]