from django.shortcuts import render
from .models import Book
from .forms import BookForm
# Create your views here.


def main(request):

    

    form = BookForm()

    if request.method == "POST":

        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            #print(book)
            #user = request.user
            #   print(user)
            #user.books_read.add(book)  
    else:
        form = BookForm()

    return render(request, "BookHub/main.html", context={'form':form})