
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abc/',include('labrary.urls')),
    path('',include('student.urls')),
]
