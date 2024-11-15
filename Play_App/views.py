from django.shortcuts import render, get_object_or_404, redirect
from .models import Word
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import datetime
import jdatetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max, Q


@csrf_exempt
@login_required
def game_show(request):
    date_get = jdatetime.datetime.now().date()
    date = date_get.strftime("%Y/%m/%d")

    # Find the maximum day that the user has in their words
    max_day = Word.objects.filter(user=request.user).aggregate(max_day=Max('day'))['max_day']
    
    # If max_day is None (meaning no words for the user), set it to 0 or show an error message
    if max_day is None:
        return render(request, "Play_App/service.html", {
            'set_up_error': 'لطفاً ابتدا کلمه‌ای اضافه کنید.',
            'date': date
        })

    # Find the first available word for the current or previous day that is unlocked
    word = Word.objects.filter(
        user=request.user,
        day__lte=max_day,  # Only fetch words up to the max day level
    ).filter(
        Q(lock_time__isnull=True) | Q(lock_time__lt=timezone.now() - datetime.timedelta(hours=12))  # Check for unlocked words
    ).order_by('day').first()
    print(word)

    # Check if all words have been answered correctly and are within the 12-hour lock period
    all_words_answered = not Word.objects.filter(
        user=request.user,
        day__lte=max_day,
        is_correct=False
    ).exists()

    # If no word is available, prompt user to add a word
    if all_words_answered:
        return render(request, "Play_App/service.html", {
            'finish_error': 'شما به همه کلمات پاسخ داده‌اید. لطفاً ۱۲ ساعت صبر کنید تا دوباره بتوانید بازی کنید.',
            'date': date
        })
        
    elif not word:
        return render(request, "Play_App/service.html", {
            'daily_error': 'لطفاً ابتدا کلمه‌ای اضافه کنید.',
            'date': date
        })



    if request.method == "POST":
        data = json.loads(request.body)
        word_id = data.get("word_id")
        is_correct = data.get("is_correct")

        word = get_object_or_404(Word, id=word_id, user=request.user)

        # Ensure the word hasn't been reviewed in the last 12 hours
        if word.lock_time and timezone.now() - word.lock_time < datetime.timedelta(hours=12):
            return JsonResponse({'success': False, 'message': 'هنوز ۱۲ ساعت نگذشته است.'})

        # Update the word based on correctness
        if is_correct:
            word.day += 1
            if word.day > 30:
                word.delete()
                return JsonResponse({'success': True, 'message': 'کلمه بعد از ۳۰ روز حدس درست حذف شد.', 'action': 'remove'})
        else:
            word.day = 1

        word.update_box()  # Assuming update_box() is a method on the Word model
        word.is_correct = is_correct
        word.lock_time = timezone.now()  # Set lock time to prevent access for 12 hours
        word.save()

        return JsonResponse({'success': True, 'message': 'کلمه به‌روز شد', 'action': 'update', 'day': word.day})

    return render(request, "Play_App/service.html", {'word': word, 'date': date})





















@csrf_exempt
@login_required
def delete_word(request):
    if request.method == "POST":
        data = json.loads(request.body)
        word_id = data.get("word_id")

        # Retrieve the word associated with the logged-in user
        word = get_object_or_404(Word, id=word_id, user=request.user)

        # Delete the word
        word.delete()

        return JsonResponse({'success': True, 'message': 'Your word deleted !'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request.'})

@login_required
def add_word_show(request):
    try:
        date_get = jdatetime.datetime.now().date()
        date = date_get.strftime("%Y/%m/%d")
        max_day = Word.objects.filter(user=request.user).aggregate(max_day=Max('day'))['max_day']
        
        # Check if all words have been answered correctly and are within the 12-hour lock period
        all_words_answered = not Word.objects.filter(
            user=request.user,
            day__lte=max_day,
            is_correct=False
        ).exists()

        # If no word is available, prompt user to add a word
        if all_words_answered:
            return render(request, "Play_App/service.html", {
                'finish_error': 'شما به همه کلمات پاسخ داده‌اید. لطفاً ۱۲ ساعت صبر کنید تا دوباره بتوانید بازی کنید.',
                'date': date
            })
            
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
        
        
    except:    
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
    
    
def edit_word(request, id):
    word_info = get_object_or_404(Word, id=id)

    if request.method == "POST":
        # Get form data
        front_word = request.POST.get('front_word')
        back_word = request.POST.get('back_word')
        back_word_day = request.POST.get('back_word_day')  # Corrected name of day input field
        back_word_box = request.POST.get('back_word_box')  # Box value

        # Ensure valid integer conversion for back_word_day and back_word_box
        if back_word_day:
            try:
                back_word_day = int(back_word_day)
            except ValueError:
                back_word_day = 1  # Default value if invalid input
        else:
            back_word_day = 1  # Default value if not provided

        # The box should be calculated based on the 'day' value
        word_info.front_word = front_word
        word_info.back_word = back_word
        word_info.day = back_word_day

        # Use the update_box method to update the box value
        word_info.update_box()

        word_info.save()

        return redirect('Play_App:game')

    return render(request, 'Play_App/edit_word.html', {'word_info': word_info})
