from django.contrib import admin
from .models import Font, FirstPageText, BenfitText, GuideText, LearningEnglishText, GuideInfo

class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Font)
class FontAdmin(ReadOnlyAdmin):
    list_display = ('id', 'font',)

@admin.register(FirstPageText)
class FirstPageTextAdmin(ReadOnlyAdmin):
    list_display = ('id', 'big_title_1', 'small_title_1', 'big_title_2', 'small_title_2', 'big_title_3', 'small_title_3')

@admin.register(BenfitText)
class BenfitTextAdmin(ReadOnlyAdmin):
    list_display = ('id', 'main_topic', 'topic_1', 'info_1', 'topic_2', 'info_2', 'topic_3', 'info_3', 'topic_4', 'info_4')

@admin.register(GuideText)
class GuideTextAdmin(ReadOnlyAdmin):
    list_display = ('id', 'main_topic', 'guide_text')

@admin.register(LearningEnglishText)
class LearningEnglishTextAdmin(ReadOnlyAdmin):
    list_display = ('id', 'main_topic', 'left_big_title', 'left_small_title', 'right_big_title', 'right_small_title')

@admin.register(GuideInfo)
class GuideInfoAdmin(ReadOnlyAdmin):
    list_display = ('id', 'left_title', 'left_text', 'right_title', 'right_text')
