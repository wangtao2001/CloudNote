from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index_view(request: HttpRequest):
    is_login = True
    if request.session.get('uid'):
        username = request.session['username']
    elif request.COOKIES.get('uid'):
        username = request.COOKIES['username']
    else:
        is_login = False

    return render(request, 'index/index.html', locals())
