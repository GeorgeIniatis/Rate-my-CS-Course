# Generated by Django 2.2.3 on 2020-03-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserating',
            name='dateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
