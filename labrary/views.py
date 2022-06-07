from ast import Return
from django.shortcuts import render,redirect
from django.http import HttpResponse
from labrary.models import Admininfo
from labrary.models import Book


# Create your views here.
    

def Signup(request):
    if(request.method=="GET"):
        return render(request,"signup.html",{})
    else:
        username=request.POST["uname"]
        pwd=request.POST["pwd"]
        email=request.POST["email"]
        user=Admininfo(username,pwd,email)
        user.save()
        return redirect(Login)
    
def Login(request):
    if(request.method=="GET"):
        return render(request,"login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            u1 = Admininfo.objects.get(user=uname,passworld=pwd)
            return  redirect(showallbook)
        except:
            return  redirect(Login) 
def showallbook(request):
    book= Book.objects.all()
    return render(request,"ShowallBook.html",{"book":book})
    
def addbook(request):
    if(request.method=="GET"):
        return render(request,"addbook.html",{})
    else: 
            
            bname= request.POST["bname"]
            author = request.POST["author"]
            price=request.POST["price"]
            b = Book()
            b.bname = bname
            b.author = author
            b.price = price
            b.save()
            return redirect(showallbook)
def editbook(request,id):
    b= Book.objects.get(id=id)
    if(request.method == "GET"):
        return render(request,"EditBook.html",{'book':b})
    else:
        b.bname= request.POST["bname"]
        b.author= request.POST["author"]
        b.price=request.POST["price"]
        b.save()
        return redirect(showallbook)

    
def deletebook(request,id):
    b= Book.objects.get(id=id)
    if(request.method == "GET"):
        return render(request,"deleteconfirm.html",{'book':b})
    else:
        action = request.POST["task"]
    if(action == "Yes"):
            b.delete()
    return redirect(showallbook)
        
  