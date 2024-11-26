from django.shortcuts import render
from .models import BookDetails
# Create your views here.

def index(request):
    #front end location 
    return render(request,'books/index.html')