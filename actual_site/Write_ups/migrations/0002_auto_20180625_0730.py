# Generated by Django 2.0.6 on 2018-06-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Write_ups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='write_up',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date made'),
        ),
    ]
