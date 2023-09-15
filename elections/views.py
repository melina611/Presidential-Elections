from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .forms import UserForm, LoginForm

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "elections/home.html")
            else:
               messages.error(request, "Incorrect username or password")
               return redirect("/")    
    context = {'form': LoginForm}
    return render(request, "elections/login_user.html", context)  

def signUp(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email_address']
            createPassword = form.cleaned_data['create_password']
            confirmPassword = form.cleaned_data['confirm_password']

            error = False

            existing_username = User.objects.filter(username=username).first()
            if existing_username:
                error = True
                messages.error(request, "This username already exists")
            existing_email = User.objects.filter(email=email).first()
            if existing_email:
                error = True
                messages.error(request, "This email address is already registered")
            if createPassword != confirmPassword:
                error = True
                messages.error(request, "Passwords do not match")

            if error:
                return redirect("signUp")

            users = User.objects.create_user(username, email, createPassword)
            users.first_name = firstName
            users.last_name = lastName
            users.save()  
            return redirect("home") 
        
    context = {'form': UserForm}
    return render(request, "elections/signUp.html", context)


def home(request):
    return render(request, "elections/home.html")
