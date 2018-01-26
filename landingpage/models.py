from django.db import models
from django.utils import timezone

class New(models.Model):
    title = models.CharField( max_length = 150 )
    about = models.CharField( max_length = 150 )

    def __str__(self):
        return str(self.title)

class Work(models.Model):
    work_type = models.CharField( max_length = 150 )
    about = models.CharField( max_length = 150 )

    def __str__(self):
        return self.work_type

class Application(models.Model):
    fio = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    works = models.ForeignKey('Work', null = True, on_delete = models.SET_NULL)
    comment = models.CharField(max_length=150, default='None')

    def __str__(self):
        return self.fio
