from django.urls import path
from MyApp.views import main_page, countries_list_view


urlpatterns = [
    path('', main_page, name='main-page'), 
    
    path('countries-list/', countries_list_view, name='countries-list'),  
 
]
