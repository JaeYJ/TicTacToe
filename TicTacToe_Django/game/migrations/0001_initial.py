# Generated by Django 4.0.5 on 2022-06-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Played',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(max_length=24)),
                ('decisions', models.CharField(max_length=12)),
            ],
        ),
    ]
