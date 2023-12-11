from django.contrib import admin
from django.urls import path, include
from cities.views import CityDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),


]
