from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200,default="Enter title")
    author = models.CharField(max_length=50,default="Enter author")
    content = models.TextField(default="Add content")
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    # def __str__(self):
    #     return self.title

    def snippet(self):
        return self.content[:50] + '...'

