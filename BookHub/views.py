from django.shortcuts import render
from .models import Book
from .forms import BookForm
from users.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings

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



    return render(request, "BookHub/main.html", context={'form':form, "user_books" : user_books})



# def book(request, book_id):
#     get_book_name = get_object_or_404(Book, id = book_id)
#    #book = f'{settings.BASE_DIR}{settings.MEDIA_URL}{get_book_name}'
#    #book = f"{settings.MEDIA_URL}{book_name}"
#     book = request.build_absolute_uri(f"{settings.MEDIA_URL}{get_book_name.path}")
#     print(book)
#     return render(request, "BookHub/book.html", context={"book":book})