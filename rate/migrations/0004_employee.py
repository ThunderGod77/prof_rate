# Generated by Django 3.0.3 on 2020-03-19 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0003_auto_20200318_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('user_photo', models.CharField(blank=True, max_length=50, null=True)),
                ('user_rating', models.IntegerField(default=0)),
                ('is_blocked', models.BooleanField(default=False)),
                ('block_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
