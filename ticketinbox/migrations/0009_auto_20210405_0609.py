# Generated by Django 2.2.12 on 2021-04-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0008_auto_20210405_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='due_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]