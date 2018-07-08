# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20160308_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='gratuity',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=4, blank=True),
        ),
    ]
