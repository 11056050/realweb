from django.db import models

# Create your models here.
class Book(models.Model):
    booktitle = models.CharField(max_length=200)
    picture = models.TextField()
    info = models.TextField()
    creator = models.TextField()
    release = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pub_date', )
    
    def __str__(self) -> str:
        return self.booktitle