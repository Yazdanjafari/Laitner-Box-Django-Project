from django.shortcuts import render
import jdatetime

def game_show (request):
    current_date = jdatetime.datetime.now()
    date = current_date.strftime('%Y/%m/%d')
    return render(request, "Play_App/service.html", context={"date":date,})

def add_word_show (request):
    return render(request, "Play_App/word.html")

