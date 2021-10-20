from django.shortcuts import render
from django.http import *
from . import models
import hashlib

# Create your views here.


def register_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if models.User.objects.filter(username=username):
            context = {
                'tips': '用户名已存在'
            }
            return render(request, 'user/register.html', context=context)
        m = hashlib.md5()
        m.update(password1.encode())
        password = m.hexdigest()
        models.User.objects.create(username=username, password=password)
        return HttpResponse('注册成功')  # 做一个重定向
    else:
        pass
