from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('clients/', views.clients_search, name='search'),
    path('registration/', views.registration_view, name='registration'),
    path('registration_procedure/', views.registration_procedure, name='registration_procedure'),
    path('<str:first_name>/<int:id>/', views.client_card, name='client_card'),
]