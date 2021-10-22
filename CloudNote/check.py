from django.http import HttpResponseRedirect, HttpRequest


def login_check(func):
    def wrap(request: HttpRequest, *args, **kwargs):
        if not request.session.get('username') or not request.session.get('uid'):
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_uid or c_username:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = c_username
                request.session['c_uid'] = c_uid
        return func(request, *args, **kwargs)
    return wrap
