# Generated by Django 4.0.5 on 2022-06-26 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Game_Played',
        ),
    ]
