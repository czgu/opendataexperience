from api.models import NutritionMeasureUnits

units = [
    ('weight','g'),
    ('energy','kJ'),
    ('protein','g'),
    ('carbonhydrate','g'),
    ('total_sugar','g'),
    ('total_dietary_fibre','g'),
    ('total_fat','g'),
    ('saturated_fat','g'),
    ('cholesterol','mg'),
    ('calcium','mg'),
    ('iron','mg'),
    ('sodium','mg'),
    ('potassium','mg'),
    ('magnesium','mg'),
    ('phosphorus','mg'),
    ('vitaminA','mg'),
    ('vitaminC','mg'),
    ('alcohol','g'),
    ('caffeine','mg')
]

for unit in units:
    n = NutritionMeasureUnits(
        nutrient_type=unit[0],
        nutrient_unit=unit[1]
    )
    n.save()
