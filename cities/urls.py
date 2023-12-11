from django.urls import path
from cities import views
from cities.views import CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', CityListView.as_view(), name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('add/', CityCreateView.as_view(), name='add'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
]
