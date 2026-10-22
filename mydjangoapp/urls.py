from django.urls import path, include
from mydjangoapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('status/', views.status, name='status'),
]