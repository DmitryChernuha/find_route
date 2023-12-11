from django.urls import path

from cities import views

urlpatterns = [
    path('', views.cities, name='cities'),
]
