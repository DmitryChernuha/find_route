from django.contrib import admin
from django.urls import path, include
from routes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),
    path('', views.home, name='home'),
    path('find_routes/', views.find_routes, name='find_routes'),
]
