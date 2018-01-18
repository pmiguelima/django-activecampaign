# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-18 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_key', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(max_length=255)),
                ('sdate', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Campanha',
                'verbose_name_plural': 'Campanhas',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_key', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(max_length=255)),
                ('subscription_notify', models.CharField(blank=True, max_length=255)),
                ('unsubscription_notify', models.CharField(blank=True, max_length=255)),
                ('sender_remember', models.TextField(blank=True, null=True)),
                ('sender_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Lista',
                'verbose_name_plural': 'Listas',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_key', models.IntegerField(blank=True, default=0, null=True)),
                ('subject', models.CharField(max_length=255)),
                ('html', models.TextField()),
                ('list_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activecampaign.List')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='list_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activecampaign.List'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activecampaign.Message'),
        ),
    ]
