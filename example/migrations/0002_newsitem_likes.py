# Generated by Django 4.0.5 on 2022-06-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
