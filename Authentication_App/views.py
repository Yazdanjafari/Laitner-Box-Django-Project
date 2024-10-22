from django.shortcuts import render

def signup_show (request):
    return render(request, "Authentication_App/signup.html")

def login_show (request):
    return render(request, "Authentication_App/login.html")


