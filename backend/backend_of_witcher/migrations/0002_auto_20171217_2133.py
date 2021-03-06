# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend_of_witcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(default="there must be a description, but it don't. sorry )':"),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]
