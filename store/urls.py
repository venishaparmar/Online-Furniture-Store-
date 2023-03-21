from django.contrib import admin
from django.urls import path
from store import views
from . import views

urlpatterns = [
    # path('',views.index,name='homepage'),
    path('',views.home,name='Home'),
    # path('#',views.home,name='Home'),
    path('sofa',views.sofa,name='Sofa'),
    path('bed',views.bed,name='Bed'),
    path('dinning',views.dinning,name='Dinning'),
    path('tables',views.tables,name='Tables'),
    path('chairs',views.chairs,name='Chairs'),
    path('shelves',views.shelves,name='Shelves'),
    path('lamps',views.lamps,name='Lamps'),
]
