from django.shortcuts import render
from .models import Book
from .forms import BookForm
from users.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings

import pdfplumber
#import requests
from bs4 import BeautifulSoup


# import pdfplumber 

# Create your views here.


def main(request):

    get_user = User.objects.all().filter(id = request.user.id)
    user_books = get_user[0].books_read.all()

    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            user = request.user
            user.books_read.add(book)  
    else:
        form = BookForm()



    def get_pages(file_book):
        with pdfplumber.open(file_book) as pdf:
            return len(pdf.pages)
    
    books = user_books
    print(books)
    for book in books:
        book.page = get_pages(str(f'media/{book.path}'))
        book.save()
        # book = Book.objects.filter(path=i).update(page = get_pages(str(f"media/{i}")))


    return render(request, "BookHub/main.html", context={'form':form, "user_books" : user_books})


def book(request):

    return render(request, "BookHub/book.html")
