from django.shortcuts import render, redirect
from .models import Book, ChekDay
from .forms import BookForm, ChekDayForm
from users.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.paginator import Paginator


import requests
import time
from bs4 import BeautifulSoup





import pdfplumber



# import pdfplumber 

# Create your views here.


def main(request):

    get_user = User.objects.all().filter(id = request.user.id)
    user_books = get_user[0].books_read.all()

    page = request.GET.get("page", 1)

    user_paginator = Paginator(user_books, 4)
    user_books = user_paginator.page(page)

    form_book = BookForm()
    
    if request.method == "POST" and 'book_form' in request.POST:
        form_book = BookForm(request.POST, request.FILES)
        if form_book.is_valid():
            book = form_book.save()
            user = request.user
            user.books_read.add(book)  
    else:
        form_book = BookForm()

    read_pages = 0

    form_read = ChekDayForm()


    if request.method == "POST" and 'read_form' in request.POST:
       
        form_read = ChekDayForm(request.POST)
        if form_read.is_valid():
            
            curent_book = request.POST['book_id']
            read_pages = request.POST["count_of_read_pages"]


            book_id = get_object_or_404(Book, id = curent_book)
            a = ChekDay.objects.create(count_of_read_pages=read_pages)
            a.book.add(book_id)
            a.save()
            
            
            redirect('/')
    else:
        form_read = ChekDayForm()


    def get_pages(file_book):
        with pdfplumber.open(file_book) as pdf:
            return len(pdf.pages)
    
    # books = user_books    
    # print(books)
    # for book in books:
    #     book.page = get_pages(str(f'media/{book.path}'))
    #     book.save()
        # book = Book.objects.filter(path=i).update(page = get_pages(str(f"media/{i}")))


        # Парсим страницу на которые мы находимся

        

       # print(soup)

    
    


    return render(request, "BookHub/main.html", context={'form_book':form_book, "form_read":form_read,"read_pages":read_pages, "user_books" : user_books, "page_range": user_paginator.page_range})


def book(request):

    return render(request, "BookHub/book.html")


# def count_of_read_pages(request):

#     form_book = ChekDayForm()

    
    
#     if request.method == "POST":
#         print(request.POST)
#         form_book = ChekDayForm(request.POST)
#         if form_book.is_valid():
#             form_book.save()
#     else:
#         form_book = ChekDayForm()

#     return render(request, "BookHub/main.html", context={"form_read":form_book})



def check_days(request):
    check1 = ChekDay.objects.all()

    local_time = time.localtime().tm_mday
    read_today = 0

    for i in check1:
        if i.day.day == local_time:
            read_today += i.count_of_read_pages

    print(read_today)


    return render(request, "BookHub/days.html", context={"check":check1, "read_today" : read_today, "days":range(365)})