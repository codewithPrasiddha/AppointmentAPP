from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.All, name="Get"),
    path('single/<str:pk>/',
         views.Single, name="Details"),
    path('add/', views.Add, name="Store"),
    path('edit/<str:pk>/',
         views.Edit, name="Edit"),
    path('remove/<str:pk>/',
         views.Remove, name="Remove"),
    path('ratings', views.AllRating, name="GetR"),
    path('ratings-single/<str:pk>/',
         views.SingleRating, name="DetailsR"),
    path('ratings-add/', views.AddRating, name="StoreR"),

]
