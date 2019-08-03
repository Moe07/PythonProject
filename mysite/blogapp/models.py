from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=20)
    author_bio = models.CharField(max_length=200)
     # ...
    def __str__(self):
        return self.author_name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=2000)
    date_created = models.DateTimeField('date created')
     # ...
    def __str__(self):
        return self.title_text


