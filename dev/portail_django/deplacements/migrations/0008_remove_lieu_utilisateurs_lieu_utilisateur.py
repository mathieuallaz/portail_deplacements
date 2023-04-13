# Generated by Django 4.2 on 2023-04-11 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deplacements', '0007_alter_taux_options_alter_taux_taux'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lieu',
            name='utilisateurs',
        ),
        migrations.AddField(
            model_name='lieu',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]