from django.shortcuts import render
from .models import Athlete
from django.http import HttpResponse
from random import shuffle

# Create your views here.


def index(request):
    return render(request, 'draw/index.html')


def submit(request):
    name = request.POST.get('name')
    user = Athlete.objects.filter(name=name)
    if name is '':
        return render(request, 'draw/info.html', {'text': '姓名不能为空！'})
    if user.exists():
        return render(request, 'draw/info.html', {'text': '该名字已经存在！'})
    else:
        users = Athlete.objects.filter(name='')
        user = users[0]
        user.name = name
        user.save()
        return render(request, 'draw/info.html', {'text': '您的编号是：' + str(user.number)})


def _init(request):
    array = []
    for i in range(1, 129):
        array.append(i)
    shuffle(array)
    for i in array:
        user = Athlete(number=i)
        user.save()

