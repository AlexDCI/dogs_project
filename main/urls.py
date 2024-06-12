from django.urls import path
from main.views import home, add_dog

urlpatterns = [
    
    path('home/', home, name='home_page' ),
    path('add/', add_dog, name='add_dog'),
]