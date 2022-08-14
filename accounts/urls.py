from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('new/', views.new, name='new'),
]
