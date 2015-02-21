from django.db import models

class MeasureUnits(models.Model):
    nutrient_type = models.CharField(max_length=200)
    nutrient_unit = models.CharField(max_length=200)

class DetailedFoodNutritions(models.Model):
    food_name = models.CharField(max_length=200)
    measure = models.IntegerField(default=0)
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
    vitaminB = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    vitaminC = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    alcohol = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    caffeine = models.DecimalField(max_digits=10, decimal_places=4, default=0)

