# Generated by Django 4.2.17 on 2024-12-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0002_pokemon_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='user_id',
            new_name='user',
        ),
    ]
