from django.shortcuts import render

def index_show (request):
    return render(request, 'Home_App/index.html')

def about_show (request):
    return render(request, 'Home_App/about.html')

