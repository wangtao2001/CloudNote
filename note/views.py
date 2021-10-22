from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from user.models import User
from note.models import Note
from CloudNote.check import login_check

# Create your views here.


@login_check
def all_note_view(request: HttpRequest):
    user = User.objects.get(id=request.session.get('uid'))
    username = user.username
    notes = user.note_set.filter(is_active=True)
    return render(request, 'note/all_note.html', locals())


@login_check
def add_note_view(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = User.objects.get(id=request.session.get('uid'))
        user.note_set.create(title=title, content=content)
        return HttpResponseRedirect('/note/all_note')


@login_check
def delete_note(request: HttpRequest, note_id):
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        return HttpResponse('The note is not existed')
    note.is_active = False
    note.save()
    return HttpResponseRedirect('/note/all_note')


@login_check
def detail_note_view(request: HttpRequest, note_id):
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        return HttpResponse('The note is not existed')
    return render(request, 'note/detail_note.html', locals())


@login_check
def update_note_view(request: HttpRequest, note_id):
    try:
        note = Note.objects.get(id=note_id, is_active=True)
    except Exception as e:
        return HttpResponse('The note is not existed')

    if request.method == 'GET':
        return render(request, 'note/update_note.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect(f'/note/detail_note/{note.id}')
    else:
        pass
