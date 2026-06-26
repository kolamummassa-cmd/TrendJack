from django.urls import path
from . import views

app_name = 'trends'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<int:pk>/', views.trend_detail, name='trend_detail'),
]
