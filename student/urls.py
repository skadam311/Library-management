
from django.urls import path
from labrary import views
from student import views

urlpatterns = [
    path('showbook/',views.showbooks)
    
]
