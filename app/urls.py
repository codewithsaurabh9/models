from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name='index'),
    path('hello/<subid>',views.hello,name='hello'),
    path('css/',views.css,name='css')
]
