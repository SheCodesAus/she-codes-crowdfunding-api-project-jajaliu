from django.urls import path
from . import views

urlpatterns = [
    path('create-account/', views.CreateCustomUser.as_view(), name = 'create-customuser'),
    path('users/', views.CustomUserList.as_view(), name = 'customuser-list'),
    path('users/<int:pk>/', views.CustomUserDetail.as_view(), name = 'customuser-detail'),
]