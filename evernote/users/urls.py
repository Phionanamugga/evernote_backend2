from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route to home view
    path('about/', views.about, name='about'),  # Route to about view
]
