from django.urls import path, re_path
from MyApp.views import main_page, countries_list_view, country_detail_view

urlpatterns = [
    path('', main_page, name='main-page'),
    
    path('countries-list/', countries_list_view, name='countries-list'),
    re_path(r'^(?P<country>.+)/$', country_detail_view, name='country-detail'),
]