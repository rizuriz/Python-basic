from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    # path('<str:movie_id>/', views.details),
    path('about/', views.about),
    path('contact/', views.contact),

]
