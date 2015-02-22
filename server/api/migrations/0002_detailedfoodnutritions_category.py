# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailedfoodnutritions',
            name='category',
            field=models.CharField(default=b'miscellaneous foods', max_length=200),
            preserve_default=True,
        ),
    ]
