from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from testing.models import Product



# Create your views here.
def home(request):
    return render(request, 'userlogin/index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'userlogin/productview.html')
        if '@gmail.com' in username:
            user = User.objects.filter(email=username).first()
            if user is not None:                #tasmi77#tasmi@gmail.com#12345
                username = user.username
        if user is not None:
            login(request, user)
            return render(request, 'userlogin/productview.html')
        if '@admin.com' in username:
            user = User.objects.filter(email=username).first()
            if user is not None:                #sohag@admin.com#asdfg
                username = user.username
        if user is not None:
            login(request, user)
            return render(request, 'userlogin/adminhome.html')
        return render(request, 'userlogin/signin.html', {'error': 'Invalid credentials'})
    return render(request, 'userlogin/signin.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        if User.objects.filter(email=email).exists():
            return render(request, 'userlogin/signup.html', {'error': 'Email already exists'})
        
        if User.objects.filter(username=username).exists():
            return render(request, 'userlogin/signup.html', {'error': 'Username already exists'})

        if password != confirm_password:
            return render(request, 'userlogin/signup.html', {'error': 'Passwords do not match'})
        
        new_user = User.objects.create_user(username=username, email=email, password=password)

        if new_user is None:
            return render(request, 'userlogin/signup.html', {'error': 'Error creating user'})
        
        new_user.first_name = firstname
        new_user.last_name = lastname
        new_user.save()

        return render(request, 'userlogin/signin.html')

    return render(request, 'userlogin/signup.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')
def productview(request):
    products = Product.objects.all()
    return render(request, 'userlogin/productview.html', {'products': products})