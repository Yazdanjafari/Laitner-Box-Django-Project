from django.shortcuts import render

def game_show (request):
    return render(request, "Play_App/service.html")

def add_word_show (request):
    return render(request, "Play_App/word.html")
