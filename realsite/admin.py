from django.contrib import admin
from realsite.models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('booktitle', 'picture', 'info', 'creator', 'pub_date', 'release')
    
admin.site.register(Book, BookAdmin)