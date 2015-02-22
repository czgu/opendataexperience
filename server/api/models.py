from django.core import serializers
from django.db import models
from django.forms.models import model_to_dict


class NutritionMeasureUnits(models.Model):
    nutrient_type = models.CharField(max_length=200)
    nutrient_unit = models.CharField(max_length=200)

class FoodCategory(models.Model):
    category_name = models.CharField(max_length=200)

class FoodCategorySpec(models.Model):
    category_name = models.CharField(max_length=200)
    general_category = models.ForeignKey(FoodCategory)

class DetailedFoodNutritions(models.Model):
    food_name = models.CharField(max_length=200)
    category = models.ForeignKey(FoodCategorySpec)
    measure = models.IntegerField(default=1)
    unit = models.CharField(max_length=10, default='')
    weight = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    energy = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    protein = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    carbonhydrate = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    total_sugar = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    total_dietary_fibre = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    total_fat = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    saturated_fat = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    calcium = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    iron = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    sodium = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    potassium = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    magnesium = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    phosphorus = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    vitaminA = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    vitaminC = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    alcohol = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    caffeine = models.DecimalField(max_digits=10, decimal_places=4, default=0)

    def toDict(self):
        _dict = model_to_dict(self)
        del _dict['category']
        _dict['general_category'] = self.category.general_category.category_name
        _dict['specific_category'] = self.category.category_name

        return _dict

