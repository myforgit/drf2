from django.contrib import admin
from django.urls import path, include

from app import views


urlpatterns = [
    path("clas/<str:id>/",views.clas.as_view()),
    path("clas/",views.clas.as_view()),
    path("declas/",views.declas.as_view())
]