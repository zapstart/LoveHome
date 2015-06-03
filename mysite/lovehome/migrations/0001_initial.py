# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_text',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('b_created_time', models.TimeField(auto_now_add=True)),
                ('b_update_time', models.TimeField(auto_now=True)),
                ('blog_content', models.TextField(blank=True)),
            ],
        ),
    ]
