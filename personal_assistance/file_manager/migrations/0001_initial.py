# Generated by Django 4.0.1 on 2022-01-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('comment', models.CharField(max_length=1000)),
                ('type', models.CharField(choices=[('doc', 'Документы'), ('tb', 'Таблицы'), ('zip', 'Архивы'), ('img', 'Изображения'), ('mp3', 'Аудио'), ('avi', 'Видео'), ('dr', 'Другое')], default='dr', max_length=3, verbose_name='Тип файла')),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
                ('url', models.FileField(upload_to='upload/')),
            ],
        ),
    ]
