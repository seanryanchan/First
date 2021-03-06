# Generated by Django 2.0.6 on 2018-06-25 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Write_up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=2048)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
