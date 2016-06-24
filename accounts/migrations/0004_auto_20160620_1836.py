# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0003_account_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True, related_query_name='user'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True, related_query_name='user'),
        ),
    ]
