from datetime import datetime, date

from django.db import connection
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"my_templates/index.html")

def supplies_code(request):
    return render(request,"my_templates/supplies_code.html")
