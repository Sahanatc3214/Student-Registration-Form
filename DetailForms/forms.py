from django import forms
from. models import InputForm

class Details(forms.ModelForm):
    detail=InputForm()
    class Meta:
        model=InputForm
       
        fields = "__all__"
        search_fields=('first_name',)


