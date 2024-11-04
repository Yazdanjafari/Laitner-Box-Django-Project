from django.shortcuts import render
from Text_App.models import FirstPageText, BenfitText, GuideText, LearningEnglishText, GuideInfo

def index_show (request):
    FirstPageText_db = FirstPageText.objects.all()
    BenfitText_db = BenfitText.objects.all()
    LearningEnglishText_db = LearningEnglishText.objects.all()
    GuideText_db = GuideText.objects.all()
    return render(request, 'Home_App/index.html', context={
                                                            'FirstPageText_db': FirstPageText_db,
                                                            'BenfitText_db': BenfitText_db,
                                                            'LearningEnglishText_db': LearningEnglishText_db,
                                                            'GuideText_db': GuideText_db,
                                                            })


def about_show (request):
    GuideText_db = GuideText.objects.all()
    GuideInfo_db = GuideInfo.objects.all()
    return render(request, 'Home_App/about.html', context={
                                                            'GuideText_db': GuideText_db,
                                                            'GuideInfo_db': GuideInfo_db,
                                                            })