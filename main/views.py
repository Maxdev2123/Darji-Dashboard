from django.shortcuts import render



def Index(request):
    return render(request,'index.html')

def Profile(request):
    return render(request,'edit-profile.html')

def Login(request):
    return render(request,'login.html')

def Register(request):
    return render(request,'register.html')

def page_login(request):
    return render(request,'page-login.html')

def task(request):
    return render(request,'task.html')

def add_blog(request):
    return render(request,'add_blog.html')
def profile(request):
    return render(request,'profile.html')
def sales(request):
    return render(request,'sales.html')

def gallery(request):
    return render(request,'gallery.html')