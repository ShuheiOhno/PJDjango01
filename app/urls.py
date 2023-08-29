from django.urls import path
from app import views

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
]