# Generated by Django 2.2.12 on 2021-04-07 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20210407_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executive',
            name='ticket_assigned',
        ),
    ]