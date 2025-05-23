# Generated by Django 5.1.2 on 2024-11-03 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Text_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benfittext',
            options={'verbose_name_plural': 'متن\u200cهای فایده\u200cها (صفحه اصلی)'},
        ),
        migrations.AlterModelOptions(
            name='firstpagetext',
            options={'verbose_name_plural': 'متن\u200cهای صفحه اول (صفحه اصلی)'},
        ),
        migrations.AlterModelOptions(
            name='font',
            options={'verbose_name_plural': 'فونت\u200cها (صفحه اصلی)'},
        ),
        migrations.AlterModelOptions(
            name='guideinfo',
            options={'verbose_name_plural': 'توضیحات راهنما (صفحه راهنما)'},
        ),
        migrations.AlterModelOptions(
            name='guidetext',
            options={'verbose_name_plural': 'متن\u200cهای راهنما (صفحه اصلی و راهنما)'},
        ),
        migrations.AlterModelOptions(
            name='learningenglishtext',
            options={'verbose_name_plural': 'متن\u200cهای یادگیری انگلیسی (صفحه اصلی)'},
        ),
        migrations.AddField(
            model_name='benfittext',
            name='info_4',
            field=models.TextField(default='fix it please', verbose_name='توضیحات بخش 4'),
        ),
        migrations.AddField(
            model_name='benfittext',
            name='main_topic',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='موضوع'),
        ),
        migrations.AddField(
            model_name='benfittext',
            name='topic_4',
            field=models.CharField(default='fix it please', max_length=16, verbose_name='موضوع بخش 4'),
        ),
        migrations.AddField(
            model_name='guidetext',
            name='main_topic',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='موضوع'),
        ),
        migrations.AddField(
            model_name='learningenglishtext',
            name='main_topic',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='benfittext',
            name='info_1',
            field=models.TextField(default='fix it please', verbose_name='توضیحات بخش 1'),
        ),
        migrations.AlterField(
            model_name='benfittext',
            name='info_2',
            field=models.TextField(default='fix it please', verbose_name='توضیحات بخش 2'),
        ),
        migrations.AlterField(
            model_name='benfittext',
            name='info_3',
            field=models.TextField(default='fix it please', verbose_name='توضیحات بخش 3'),
        ),
        migrations.AlterField(
            model_name='benfittext',
            name='topic_1',
            field=models.CharField(default='fix it please', max_length=16, verbose_name='موضوع بخش 1'),
        ),
        migrations.AlterField(
            model_name='benfittext',
            name='topic_2',
            field=models.CharField(default='fix it please', max_length=16, verbose_name='موضوع بخش 2'),
        ),
        migrations.AlterField(
            model_name='benfittext',
            name='topic_3',
            field=models.CharField(default='fix it please', max_length=16, verbose_name='موضوع بخش 3'),
        ),
        migrations.AlterField(
            model_name='firstpagetext',
            name='big_title_1',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن اصلی 1'),
        ),
        migrations.AlterField(
            model_name='firstpagetext',
            name='big_title_2',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن اصلی 2'),
        ),
        migrations.AlterField(
            model_name='firstpagetext',
            name='big_title_3',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن اصلی 3'),
        ),
        migrations.AlterField(
            model_name='firstpagetext',
            name='small_title_1',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن فرعی 1'),
        ),
        migrations.AlterField(
            model_name='firstpagetext',
            name='small_title_2',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن فرعی 2'),
        ),
        migrations.AlterField(
            model_name='firstpagetext',
            name='small_title_3',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن فرعی 3'),
        ),
        migrations.AlterField(
            model_name='font',
            name='font',
            field=models.CharField(choices=[('فونت پرستو', 'فونت پرستو'), ('فونت ساحل', 'فونت ساحل'), ('فونت صمیم', 'فونت صمیم'), ('(پیشنهاد) فونت تنها', '(پیشنهاد) فونت تنها'), ('فونت وزیر', 'فونت وزیر'), ('فونت یکان', 'فونت یکان')], default='fix it please', max_length=50, verbose_name='فونت'),
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='left_pic',
            field=models.ImageField(default='fix it please', upload_to='web_pics', verbose_name='تصویر چپ'),
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='left_text',
            field=models.TextField(default='fix it please', verbose_name='متن چپ'),
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='left_title',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='موضوع بخش سمت چپ'),
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='right_pic',
            field=models.ImageField(default='fix it please', upload_to='web_pics', verbose_name='تصویر راست'),
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='right_text',
            field=models.TextField(default='fix it please', verbose_name='متن راست'),
        ),
        migrations.AlterField(
            model_name='guideinfo',
            name='right_title',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='موضوع بخش سمت راست'),
        ),
        migrations.AlterField(
            model_name='guidetext',
            name='guide_text',
            field=models.TextField(default='fix it please', verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='learningenglishtext',
            name='left_big_title',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن اصلی چپ'),
        ),
        migrations.AlterField(
            model_name='learningenglishtext',
            name='left_small_title',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن فرعی چپ'),
        ),
        migrations.AlterField(
            model_name='learningenglishtext',
            name='right_big_title',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن اصلی راست'),
        ),
        migrations.AlterField(
            model_name='learningenglishtext',
            name='right_small_title',
            field=models.CharField(default='fix it please', max_length=55, verbose_name='متن فرعی راست'),
        ),
    ]
