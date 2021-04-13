# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 23:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(default='', max_length=200)),
                ('School', models.CharField(default='', max_length=20)),
                ('College', models.CharField(default='', max_length=20)),
                ('About_me', models.CharField(default='', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
