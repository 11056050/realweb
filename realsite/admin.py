from django.contrib import admin
<<<<<<< HEAD
from realsite.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('booktitle', 'picture', 'info', 'creator', 'pub_date', 'release')
    
admin.site.register(Book, BookAdmin)
=======
from realsite.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
    
admin.site.register(Post, PostAdmin)
>>>>>>> ce533d24d56688f151f2b28cf6f110fdd6654e69

