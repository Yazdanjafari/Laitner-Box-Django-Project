from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Word
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import datetime, jdatetime

@csrf_exempt
@login_required
def game_show(request):
    date_get = jdatetime.datetime.now().date()
    date = date_get.strftime("%Y/%m/%d")
    if request.method == "POST":
        word_id = request.POST.get("word_id")
        is_correct = request.POST.get("is_correct") == "true"

        word = get_object_or_404(Word, id=word_id, user=request.user)

        # Check if 12 hours have passed since last review
        if timezone.now() - word.last_reviewed < datetime.timedelta(hours=12):
            return JsonResponse({'success': False, 'message': 'You cannot play again yet.'})


        if is_correct:
            word.day += 1
            if word.day > 30:
                word.delete()
                return JsonResponse({'success': True, 'message': 'Word removed after 30 correct guesses', 'action': 'remove'})

        else:
            word.day = 1

        word.last_reviewed = timezone.now()
        word.save()
        return JsonResponse({'success': True, 'message': 'Word updated', 'action': 'update', 'day': word.day})

    word = Word.objects.filter(user=request.user).order_by('?').first()
    if word:
        return render(request, "Play_App/service.html", {'word': word, 'date': date})
    else:
        return render(request, "Play_App/service.html", {'error': 'No words available'})




@login_required
def add_word_show(request):
    if request.method == 'POST':
        front_word = request.POST.get('front_word')
        back_word = request.POST.get('back_word')

        if front_word and back_word:
            Word.objects.create(
                user=request.user,
                front_word=front_word,
                back_word=back_word,
                day=1,  # Default value
                box=1   # Default box value
            )
            return JsonResponse({'success': True})

        return JsonResponse({'success': False, 'message': 'Missing front or back word'})

    return render(request, "Play_App/word.html")