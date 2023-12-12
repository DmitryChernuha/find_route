from django.urls import path
from trains import views

urlpatterns = [
    path('', views.TrainListView.as_view(), name='train'),
    path('detail/<int:pk>/', views.TrainDetailView.as_view(), name='detail'),
    path('add_train/', views.TrainCreateView.as_view(), name='add_train'),
    path('update/<int:pk>', views.TrainUpdateView.as_view(), name='update'),
]
