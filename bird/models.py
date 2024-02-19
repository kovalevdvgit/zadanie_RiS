from django.db import models

# Create your models here.
class bird(models.Model):
    name = models.CharField(verbose_name='Название птицы', max_length = 100, blank=False)
    #photo = models.ImageField(verbose_name='Фото птицы', upload_to = 'media/', allow_empty_file = True)
    color_plumage = models.CharField(verbose_name='Цвет оперенья', max_length=100, blank=True)
    img = models.ImageField(verbose_name='Фото птицы', upload_to = 'media/')


    def __str__(self):
        return self.name

class view_bird(models.Model):
    bird = models.ForeignKey(bird, verbose_name="Увидел птицу", blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Время и дата', auto_now=True)

