from .models import Reviews,Data

from django import forms


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ("name","email","text")

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["name","power","drive","volume"]
