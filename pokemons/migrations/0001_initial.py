# Generated by Django 4.2.17 on 2024-12-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poke_type', models.CharField(max_length=200)),
                ('poke_name', models.CharField(max_length=200)),
            ],
        ),
    ]