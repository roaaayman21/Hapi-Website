# Generated by Django 4.1.4 on 2022-12-27 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_tracking_pack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='Pack',
        ),
    ]
