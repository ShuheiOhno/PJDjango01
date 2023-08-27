from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.ProfileEditView.as_view(), name='profile_edit'),
]