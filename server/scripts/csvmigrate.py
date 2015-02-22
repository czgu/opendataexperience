import csv
import re

from api.models import DetailedFoodNutritions
from api.models import FoodCategory
from api.models import FoodCategorySpec


def is_empty_row(row):
    return True if ''.join(row) == '' else False

with open('misc/dataset_nutrients.csv', 'rb') as csvfile:
    dataset_reader = csv.reader(csvfile)
    currentCategory = None
    currentCategorySpec = None
    #
    for element in dataset_reader:
        if len(element) != 22:
            print 'invalid row: %s' % element
        elif is_empty_row(element):
            currentCategory = None
        elif is_empty_row(element[1:]):
            if not currentCategory:
                currentCategory = FoodCategory(
                    category_name=element[0])
                currentCategory.save()
            else:
                currentCategorySpec = FoodCategorySpec(
                    category_name=element[0],
                    general_category=currentCategory
                )
                currentCategorySpec.save()
        else:
            element = map(lambda val: 0 if val == '' or val.isspace() or val == 'tr' else val , element)

            search_result = re.findall(r'\d+', element[1])
            measure = search_result[0] if len(search_result) else 1
            search_result = re.findall(r'[a-zA-Z]+', element[1])
            unit = search_result[0] if len(search_result) else 'none'

            detailed_nutrition = DetailedFoodNutritions(
                food_name=element[0],
                category=currentCategorySpec,
                measure=measure,
                unit=unit,
                weight=element[2],
                energy=element[3],
                protein=element[5],
                carbonhydrate=element[6],
                total_sugar=element[7],
                total_dietary_fibre=element[8],
                total_fat=element[9],
                saturated_fat=element[10],
                cholesterol=element[11],
                calcium=element[12],
                iron=element[13],
                sodium=element[14],
                potassium=element[15],
                magnesium=element[16],
                phosphorus=element[17],
                vitaminA=element[18],
                vitaminC=element[19],
                alcohol=element[20],
                caffeine=element[21]
            )
            print 'moved %s' % element
            detailed_nutrition.save()
