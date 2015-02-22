from django.conf.urls import patterns, url

from api.views import query
from api.views import search

urlpatterns = patterns('',
    url(r'^food/$', query.food_handler, name='food'),
    url(r'^categories/all/$', query.category_all_handler, name='category'),
    url(r'^categories/all/detailed/$', query.category_all_detailed_handler, name='category_detailed'),
    url(r'^search/food/$', search.search_food_handler, name='search_food'),
    #url(r'^search/suggestion/$', search.search_suggestion_handler, name='search_suggestion')
)

