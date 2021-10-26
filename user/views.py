from django.db.utils import IntegrityError
from django.shortcuts import render
from django.http import *
from django.utils.datastructures import MultiValueDict

from . import models
import hashlib

# Create your views here.


def register_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        if models.User.objects.filter(username=username):
            return render(request, 'user/register.html', context={'tips': '用户名已存在'})
        m = hashlib.md5()
        m.update(password1.encode())
        password = m.hexdigest()
        try:
            user = models.User.objects.create(username=username, password=password)
        except IntegrityError as e:
            return render(request, 'user/register.html', context={'tips': '用户名已存在'})

        request.session['username'] = username
        request.session['uid'] = user.id

        return HttpResponseRedirect('/')
    else:
        pass


def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.session.get('username') and request.session.get('uid'):
            return HttpResponseRedirect('/')
        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            return HttpResponseRedirect('/')

        # 直接访问login界面的时候next参数为空
        next_ = request.GET.get('next')
        if not next_:
            next_ = ""
        return render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        try:
            user = models.User.objects.get(username=username)
        except models.User.DoesNotExist as e:
            return render(request, 'user/login.html', context={'tips': '用户名或密码错误'})
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return render(request, 'user/login.html', context={'tips': '用户名或密码错误'})
        request.session['username'] = username
        request.session['uid'] = user.id

        next_ = request.GET['next']
        if next_:
            resp = HttpResponseRedirect(next_)
        else:
            resp = HttpResponseRedirect('/')
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600*24*3)
            resp.set_cookie('uid', user.id, 3600*24*3)

        return resp
    else:
        pass


def logout(request: HttpRequest):
    resp = HttpResponseRedirect('/')
    resp.delete_cookie('username')
    resp.delete_cookie('uid')
    resp.delete_cookie('sessionid')
    return resp
