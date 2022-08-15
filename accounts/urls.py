from django.urls import path
from accounts import views

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('new/', views.create, name='create'),
]
