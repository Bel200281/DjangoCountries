from django.urls import path, re_path
from MyApp.views import main_page, countries_list_view, filtered_countries_view, country_detail_view, all_languages_view

urlpatterns = [
    path('', main_page, name='main-page'),

    path('countries-list/', countries_list_view, name='countries-list'),

    path('all-languages/', all_languages_view, name='all-languages'),

    path('<str:country>/', country_detail_view, name='country-detail'), 

    path('countries/<str:letter>/', filtered_countries_view, name='filtered-countries'),
]