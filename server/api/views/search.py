from django.forms.models import model_to_dict
from django.http import JsonResponse

from api.models import FoodCategory
from api.models import FoodCategorySpec
from api.models import DetailedFoodNutritions


def search_food_handler(request):
    '''
        Request handler for retreving food from database
        Allow multiple search options

        options:{
            ordered_by: one attribute to order the result
            category: one category, can be general or specific
            filter: TODO
            only_name: boolean
        }

        return:{
            A list of food
        }
    '''
    if request.method != 'GET':
        return JsonResponse({})

    category_name = request.GET.get('category')
    if not category_name:
        raise Http404('category not provided.')

    try:
        category = FoodCategory.objects.get(category_name=category_name)
    except FoodCategory.DoesNotExist:
        try:
            category_spec = [FoodCategorySpec.objects.get(category_name=category_name)]
        except FoodCategorySpec.DoesNotExist:
            return JsonResponse({})
    else:
        category_spec = category.foodcategoryspec_set.all()

    food_items = []
    for spec in category_spec:
        food_items.extend(map(lambda x: x.toDict(), spec.detailedfoodnutritions_set.all()))

    order_by = request.GET.get('order_by')
    if len(food_items) > 1 and order_by and order_by in food_items[0].keys():
        food_items.sort(key=lambda el: el[order_by], reverse=True)

    only_name = request.GET.get('only_name')
    if only_name:
        food_items = map(lambda el: el['food_name'], food_items)

    return JsonResponse({'result': food_items})

