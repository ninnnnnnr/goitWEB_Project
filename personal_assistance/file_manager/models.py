from django.db import models


class File(models.Model):
    name = models.CharField(max_length=500)
    comment = models.CharField(max_length=1000, blank=True)
    TYPES_FILE = (
        ('doc', 'Documents'),
        ('tb', 'Tables'),
        ('zip', 'Archives'),
        ('img', 'Images'),
        ('mp3', 'Audio'),
        ('avi', 'Video'),
        ('dr', 'Other'),
    )
    type = models.CharField('Type file', max_length=3, choices=TYPES_FILE, default='dr')
    date_upload = models.DateTimeField(auto_now_add=True)
    url = models.FileField(upload_to='media/')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwarg):
        self.url.delete()
        super().delete(*args, **kwarg)

    class Meta:
        ordering = ["-date_upload"]
