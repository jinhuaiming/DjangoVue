from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='index'),
    path('queryPlaNum/', views.queryPlaNum, name='queryPlaNum'),
    path('handlePlot/', views.handlePlot, name='handlePlot'),
}
