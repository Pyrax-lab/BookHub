from django import forms 
from .models import Book,ChekDay


class BookForm(forms.ModelForm):

    class Meta:
        model = Book 
        fields = ['path']


class ChekDayForm(forms.ModelForm):

    class Meta:
        model = ChekDay
        fields = ["count_of_read_pages"]
        widgets = {
            'count_of_read_pages': forms.NumberInput(attrs={'min': 0, 'placeholder': 'Введите число страниц'}),
        }
