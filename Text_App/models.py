from django.db import models

COLOR_CHOICE = [
        ('black', 'مشکی'),
        ('#7335b7', 'بنفش'),
    ]

class Font(models.Model):
    CHOICE = [
        ('فونت پرستو', 'فونت پرستو'),
        ('فونت ساحل', 'فونت ساحل'),
        ('فونت صمیم', 'فونت صمیم'),
        ('(پیشنهاد) فونت تنها', '(پیشنهاد) فونت تنها'),
        ('فونت وزیر', 'فونت وزیر'),
        ('فونت یکان', 'فونت یکان'),
    ]
    font = models.CharField(choices=CHOICE, max_length=50, verbose_name="فونت")
    class Meta:
        verbose_name_plural = "فونت‌ها (صفحه اصلی)"


class FirstPageText(models.Model):
    big_title_1 = models.CharField(max_length=55, verbose_name="متن اصلی 1")
    small_title_1 = models.CharField(max_length=55, verbose_name="متن فرعی 1")
    big_title_2 = models.CharField(max_length=55, verbose_name="متن اصلی 2")
    small_title_2 = models.CharField(max_length=55, verbose_name="متن فرعی 2")
    big_title_3 = models.CharField(max_length=55, verbose_name="متن اصلی 3")
    small_title_3 = models.CharField(max_length=55, verbose_name="متن فرعی 3")
    class Meta:
        verbose_name_plural = "متن‌های صفحه اول (صفحه اصلی)"


class BenfitText(models.Model):
    main_topic_color = models.CharField(max_length=55, choices= COLOR_CHOICE, verbose_name= "رنگ تایتل موضوع", default= '#7335b7')
    main_topic = models.CharField(max_length=55, verbose_name="موضوع")
    topic_1 = models.CharField(max_length=16, verbose_name="موضوع بخش 1")
    info_1 = models.TextField(verbose_name="توضیحات بخش 1")
    topic_2 = models.CharField(max_length=16, verbose_name="موضوع بخش 2")
    info_2 = models.TextField(verbose_name="توضیحات بخش 2")
    topic_3 = models.CharField(max_length=16, verbose_name="موضوع بخش 3")
    info_3 = models.TextField(verbose_name="توضیحات بخش 3")
    topic_4 = models.CharField(max_length=16, verbose_name="موضوع بخش 4")
    info_4 = models.TextField(verbose_name="توضیحات بخش 4")
    class Meta:
        verbose_name_plural = "متن‌های مزیت ها (صفحه اصلی)"


class LearningEnglishText(models.Model):
    main_topic_color = models.CharField(max_length=55, choices= COLOR_CHOICE, verbose_name= "رنگ تایتل موضوع", default= '#7335b7')
    main_topic = models.CharField(max_length=55, verbose_name="موضوع")
    left_big_title = models.CharField(max_length=55, verbose_name="متن اصلی چپ")
    left_small_title = models.CharField(max_length=55, verbose_name="متن فرعی چپ")
    right_big_title = models.CharField(max_length=55, verbose_name="متن اصلی راست")
    right_small_title = models.CharField(max_length=55, verbose_name="متن فرعی راست")
    class Meta:
        verbose_name_plural = "متن‌های بخش یادگیری انگلیسی (صفحه اصلی)"


class GuideText(models.Model):
    main_topic = models.CharField(max_length=55, verbose_name="موضوع")
    guide_text = models.TextField(verbose_name="توضیحات")
    class Meta:
        verbose_name_plural = "متن‌های راهنما (صفحه اصلی و راهنما)"


class GuideInfo(models.Model):
    left_pic = models.ImageField(upload_to="web_pics", verbose_name="تصویر چپ")
    left_title = models.CharField(max_length=55, verbose_name="موضوع بخش سمت چپ")
    left_text = models.TextField(verbose_name="متن چپ")
    right_pic = models.ImageField(upload_to="web_pics", verbose_name="تصویر راست")
    right_title = models.CharField(max_length=55, verbose_name="موضوع بخش سمت راست")
    right_text = models.TextField(verbose_name="متن راست")
    class Meta:
        verbose_name_plural = "راهنما با شکل (صفحه راهنما)"
