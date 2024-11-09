from django.shortcuts import render
from .models import Book
from .forms import BookForm
from users.models import User
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