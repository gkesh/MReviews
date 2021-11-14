from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="reviews_home"),
    path('about/', views.about, name="reviews_about"),
]
