# Generated by Django 4.0.1 on 2022-01-30 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manager', '0002_alter_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='comment',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
