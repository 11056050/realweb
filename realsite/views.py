from django.shortcuts import render, redirect
from realsite.models import Book
from django.http import HttpResponse
from datetime import datetime
from .forms import PostSearchForm
from django.db.models import Q
from .forms import BookForm

# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def search_posts(request):
    form = PostSearchForm(request.GET)
    posts = Book.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        # Modify the filter to use the correct fields
        posts = posts.filter(Q(booktitle__icontains=search_query) | Q(info__icontains=search_query))

    return render(request, 'search_results.html', {'posts': posts, 'form': form})

def homepage(request):
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