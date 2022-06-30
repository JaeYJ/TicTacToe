# Generated by Django 4.0.5 on 2022-06-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game_played',
            old_name='decisions',
            new_name='lose_decisions',
        ),
        migrations.AddField(
            model_name='game_played',
            name='win_decisions',
            field=models.CharField(default=(1, 2, 3, 4), max_length=12),
            preserve_default=False,
        ),
    ]
