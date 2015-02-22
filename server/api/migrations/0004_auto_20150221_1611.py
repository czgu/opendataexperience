# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150221_1512'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MeasureUnits',
            new_name='NutritionMeasureUnits',
        ),
        migrations.RemoveField(
            model_name='detailedfoodnutritions',
            name='measure',
        ),
    ]
