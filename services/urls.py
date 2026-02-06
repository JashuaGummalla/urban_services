from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
]
