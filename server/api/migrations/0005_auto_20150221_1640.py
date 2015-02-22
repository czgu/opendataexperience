# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150221_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailedfoodnutritions',
            name='measure',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detailedfoodnutritions',
            name='unit',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
    ]
