from django.db import models


class File(models.Model):
    name = models.CharField(max_length=500)
    comment = models.CharField(max_length=1000)
    TYPES_FILE = (
        ('doc', 'Документы'),
        ('tb', 'Таблицы'),
        ('zip', 'Архивы'),
        ('img', 'Изображения'),
        ('mp3', 'Аудио'),
        ('avi', 'Видео'),
        ('dr', 'Другое'),
    )
    type = models.CharField('Тип файла', max_length=3, choices=TYPES_FILE, default='dr')
    date_upload = models.DateTimeField(auto_now_add=True)
    url = models.FileField(upload_to='upload/')


    def __str__(self):
        return self.name

