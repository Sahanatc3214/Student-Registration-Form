from .import views

from DetailForms import forms
from  DetailForms.forms import Details

from django.shortcuts  import render
from DetailForms import models
from DetailForms.models import InputForm

def home(request):
    if request.method == 'POST':
        detail=Details(request.POST,request.FILES)
       

        if detail.is_valid():
            detail.save()
    else:
        detail = Details()
    context={'details':detail}
    return render(request,'home.html',context)