from django.db import models

class Book(models.Model):
    booktitle = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='book_pictures/', blank=True, null=True)
    info = models.TextField()
    creator = models.TextField()
    release = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.booktitle