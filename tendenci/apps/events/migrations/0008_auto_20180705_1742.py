# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import timezones.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20180315_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationconfiguration',
            name='gratuity_custom_option',
            field=models.BooleanField(default=False, verbose_name='Allow users to set their own gratuity'),
        ),
        migrations.AddField(
            model_name='registrationconfiguration',
            name='gratuity_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registrationconfiguration',
            name='gratuity_options',
            field=models.CharField(default=b'17%,18%,19%,20%', help_text='Comma separated numeric numbers in percentage. A "%" will be appended if the percent sign is not present.', max_length=100, verbose_name='Gratuity Options', blank=True),
        ),
    ]
