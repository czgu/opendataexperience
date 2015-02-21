# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedFoodNutritions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_name', models.CharField(max_length=200)),
                ('measure', models.IntegerField(default=0)),
                ('weight', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('energy', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('protein', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('carbonhydrate', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('total_sugar', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('total_dietary_fibre', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('total_fat', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('saturated_fat', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('cholesterol', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('calcium', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('iron', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('sodium', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('potassium', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('magnesium', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('phosphorus', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('vitaminA', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('vitaminB', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('vitaminC', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('alcohol', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
                ('caffeine', models.DecimalField(default=0, max_digits=10, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeasureUnits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nutrient_type', models.CharField(max_length=200)),
                ('nutrient_unit', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
