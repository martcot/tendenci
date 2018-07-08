# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import timezones.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180705_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='gratuity',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=4, blank=True),
        ),
    ]
