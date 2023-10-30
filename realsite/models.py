from django.db import models

# Create your models here.
<<<<<<< HEAD
class Book(models.Model):
    booktitle = models.CharField(max_length=200)
    picture = models.TextField()
    info = models.TextField()
    creator = models.TextField()
    release = models.TextField()
=======
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length= 200)
    body = models.TextField()
>>>>>>> ce533d24d56688f151f2b28cf6f110fdd6654e69
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pub_date', )
    
    def __str__(self) -> str:
<<<<<<< HEAD
        return self.booktitle
=======
        return self.title
>>>>>>> ce533d24d56688f151f2b28cf6f110fdd6654e69
