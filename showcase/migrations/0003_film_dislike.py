# Generated by Django 3.2.9 on 2021-12-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_auto_20211205_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
    ]
