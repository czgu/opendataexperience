from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.http import Http404

from api.models import DetailedFoodNutritions
from api.models import FoodCategory
from api.models import FoodCategorySpec


def food_handler(request):
    if request.method != 'GET':
        return JsonResponse({})

    food_name = str(request.GET.get('name'))
    if not food_name:
        raise Http404('name not provided')

    try:
        food = DetailedFoodNutritions.objects.get(food_name=str(food_name))
    except DetailedFoodNutritions.DoesNotExist:
        raise Http404('food %s not found' % food_name, food_name)

    return JsonResponse(food.toDict())


def category_all_handler(request):
    if request.method != 'GET':
        return JsonResponse({})

    categories = FoodCategory.objects.all()
    return JsonResponse(
        {'categories': map(lambda e: model_to_dict(e), categories)})


def category_all_detailed_handler(request):
    if request.method != 'GET':
        return JsonResponse({})
    categories = FoodCategory.objects.all()
    formated_categories = []

    for category in categories:
        sub_categories = category.foodcategoryspec_set.all()
        formated_dict = model_to_dict(category)
        formated_dict['sub_categories'] = []
        for sub_category in sub_categories:
            _sub_dict = model_to_dict(sub_category)
            del _sub_dict['general_category']
            formated_dict['sub_categories'].append(_sub_dict)
        formated_categories.append(formated_dict)

    return JsonResponse({'categories': formated_categories})
