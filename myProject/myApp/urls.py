from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    # The path that allows to prints out all entry names
    path('allBooks/', views.allNamesBook, name="index"),
    path('allCars/', views.allNamesCar, name="index"),
    path('greaterThan2018/', views.greaterOrEqualThan01012018, name="index"),
    path('greaterThan2010/', views.greaterOrEqualThan01012010, name="index"),
]