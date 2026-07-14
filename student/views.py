import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .serializer import  StudentSerializer,AminSerializer
from .models import Student,Admin
from django.views.decorators.csrf import csrf_exempt
from .hashing import pass_hash,pass_check
# Create your views here.
def welcome(req):
    return render(req,'index.html')

def register(req):
    if req.method=='POST':
        data = req.POST.dict()
        data['password'] = pass_hash(data['password'])
        serializer = AminSerializer(data=data)
        if serializer.is_valid():
            print("Valid Data")
            serializer.save()
            return redirect('login')
        else:
            print(serializer.errors)
            return render(req, "register.html", {
                "status": serializer.errors
            })
    return render(req,'register.html')

def login(req):
    try:
        if req.method=='POST':
            obj=Admin.objects.get(email=req.POST['email'])
            check_pass=pass_check(req.POST['password'],obj.password)
            if not check_pass :
                return render(req,'login.html',{'status':'enter the password correctly'})
            else:
                serial=AminSerializer(obj)
                if not serial==None:
                    response= redirect('home')
                    response.set_cookie('is_login','True')
                    print(response)
                    return response
    except Admin.DoesNotExist:
            return HttpResponse("student details invalid")
    return render(req,'login.html')


def Home(req):
    if req.COOKIES.get("is_login") != "True":
        return render(req,"login.html",{'status':"login first"})
    students = Student.objects.all()
    return render(req, "home.html", {"student": students})

def Delete(req,input_id):
    student=Student.objects.get(rollno=input_id)
    student.delete()
    return redirect('home')

def Edit(req,input_id):
    if req.method=="POST":
        student=Student.objects.get(rollno=input_id)
        serial=StudentSerializer(student,req.POST)
        if serial.is_valid():
            serial.save()
            return redirect('home')
        else:
            return HttpResponse({"status": "invalid info"})
    return render(req,'edit.html')   

def create(req):
    if req.method=='POST':
        serializer=StudentSerializer(data=req.POST)
        if serializer.is_valid():
            print("Valid Data")
            serializer.save()
            return redirect('home')
        else:
            return render(req, "create.html", {
                "status": serializer.errors
            })
    return render(req,'create.html')


def Logout(req):
    response = redirect("/")
    response.delete_cookie("is_login")
    return response
