# Generated by Django 3.1.7 on 2021-03-18 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_steam_api', '0001_initial'),
        ('django_steam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersteam',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='steam', to='django_steam_api.player'),
        ),
        migrations.AlterField(
            model_name='usersteam',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='steam', to=settings.AUTH_USER_MODEL),
        ),
    ]
