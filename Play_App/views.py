from django.shortcuts import render
import jdatetime

def game_show (request):
    date = jdatetime.datetime.date()
    print(date)
    return render(request, "Play_App/service.html")

def add_word_show (request):
    return render(request, "Play_App/word.html")
