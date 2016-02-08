# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardsGame', '0002_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ('player',),
            },
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('user',)},
        ),
        migrations.AddField(
            model_name='card',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardsGame.Player'),
        ),
    ]
