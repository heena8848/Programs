import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import userdata
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import postwork,carausel

@login_required(login_url="signin-user")
def index(request):
    return render(request, 'index.html')

# i = 0
def dashboard(request):
    #  global i
    #  response = requests.get('https://github.com/cecyours/PythonInternShipDjnagoFeb23/blob/main/you.json').json()
    #  lst = list(response)

    #  m = lst[0]
    #  if request.method =="GET":
    #      i +=1
    #      m = lst[i]
    #      pass

    #  print(type(m))
    #  b = m[:]
    #  return render(request,'dashboard.html',{'h':m})
    return render(request,'dashboard.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    ud = userdata()
    if request.method == "POST":
        ud = userdata(request.POST)
        if ud.is_valid():
            ud.save()
            print("data saved...")

    print("Hiii..")
    return render(request, 'signup.html', {'ud': ud})
    pass


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    print("user : ", request.user)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print("welcome")
            return redirect('index')
        else:
            print("invalid username/pass")

    return render(request, 'signin.html')


def logout_(request):
    logout(request)
    return redirect('signin-user')
    pass

def get_list(request):
    list = postwork.objects.all()
    return render(request,"list.html",{"data":list})

def showsliders(request):
    return render(request,'slider.html')

def imageslider(request):
    obj= carausel.objects.all()
    context = {
        'obj' : obj
    }
    return render(request,'carausel.html',context)