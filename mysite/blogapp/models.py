from django.db import models

# Create your models here.

class Post(models.Model):
    title_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=2000)
    author_text = models.CharField(max_length=20)
    date_created = models.DateTimeField('date created')
     # ...
    def __str__(self):
        return self.title_text
  
