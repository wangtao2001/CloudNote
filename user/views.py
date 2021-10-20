from django.shortcuts import render
from django.http import *

# Create your views here.


def register_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        pass
    else:
        pass
