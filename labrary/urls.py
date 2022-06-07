
from django.urls import path
from labrary import views

urlpatterns = [
    path('signUp/',views.Signup),
    path('login/',views.Login),
    path('showallbook/',views.showallbook),
    path('addbook/',views.addbook),
    path('editbook/<id>',views.editbook),
    path('deletebook/<id>',views.deletebook),
]
