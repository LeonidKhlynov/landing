from django.db import models
from django.utils import timezone

class New(models.Model):
    title = models.CharField( max_length = 150 )
    about = models.CharField( max_length = 150 )

    def __str__(self):
        return str(self.title)
