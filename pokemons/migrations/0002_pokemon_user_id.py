# Generated by Django 4.2.17 on 2024-12-15 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to=settings.AUTH_USER_MODEL),
        ),
    ]
