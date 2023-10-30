from django.contrib import admin
from realsite.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('booktitle', 'picture', 'info', 'creator', 'pub_date', 'release')
    
admin.site.register(Book, BookAdmin)

