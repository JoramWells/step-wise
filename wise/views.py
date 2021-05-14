from django.shortcuts import render
import csv

def index(request):
    return render(request,'index.html')