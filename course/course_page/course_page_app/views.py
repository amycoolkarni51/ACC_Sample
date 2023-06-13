from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def ourcourses(request):
   return render(request, 'course.html')

def coursepage(request):
   return render(request, 'course.html')


def frontend(request):
   return render(request,'frontend.html')

def html(request):
   return render(request, 'Html.html')

def css(request):
   return render(request, "css.html")

def javascript(request):
   return render(request, "javascript.html")

def ReactJS(request):
   return render(request, "reactjs.html")

def jQuery(request):
   return render(request, "jquery.html")

def AngularJS(request):
   return render(request, "angularjs.html")


def backend(request):
   return render(request,'backend.html')

def python(request):
    return render(request,'python.html')

def java(request):
    return render(request,'java.html')

def cc(request):
    return render(request,'cc++.html')

def kotlin(request):
    return render(request,'kotlin.html')

def scale(request):
    return render(request,'scale.html')

def php(request):
    return render(request,'php.html')


def database(request):
   return render(request,'database.html')

def oracle(request):
    return render(request, 'oracle.html')

def sql(request):
    return render(request,'sql.html')

def postgresql(request):
    return render(request, 'pssql.html')

def mangodb(request):
    return render(request, 'mangodb.html')

def sqlite(request):
    return render(request, 'sqlite.html')

def sqlserver(request):
    return render(request, 'sqlserver.html')


def marketing(request):
   return render(request, 'marketing.html')

def digitalmark(request):
    return render(request, 'digital.html')

def socialmediamark(request):
    return render(request, 'social media.html')

def contentmark(request):
    return render(request, 'content mark.html')

def directmark(request):
    return render(request, 'direct mark.html')

def salesmark(request):
    return render(request, 'sales.html')

def brandmark(request):
    return render(request,'brand.html')
