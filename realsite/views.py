<<<<<<< HEAD
from django.shortcuts import render,redirect
from realsite.models import Book
=======
from django.shortcuts import render
from realsite.models import Post
>>>>>>> ce533d24d56688f151f2b28cf6f110fdd6654e69
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def homepage(request):
<<<<<<< HEAD
    posts = Book.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    
def showbook(request, book_name=None):
    if book_name:
        try:
            book = Book.objects.get(booktitle=book_name)
            return render(request, 'post.html', {'book': book})
        except Book.DoesNotExist:
            return redirect("/")
    else:
        return render(request, 'general_book.html')
=======
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    
def showpost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', locals())
    
>>>>>>> ce533d24d56688f151f2b28cf6f110fdd6654e69
"""""
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
    """