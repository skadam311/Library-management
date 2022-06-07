from ast import Return
from django.shortcuts import render,redirect
from labrary.models import Book

# Create your views here.
def showbooks(request):
    book= Book.objects.all()
    return render(request,"ShowBook.html",{"book":book})
    