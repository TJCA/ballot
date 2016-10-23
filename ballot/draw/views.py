from django.shortcuts import render
from .models import Athlete
from django.http import HttpResponse
from random import shuffle


# Create your views here.


def index(request):
    return render(request, 'draw/index.html')


def submit(request):
    name = request.POST.get('name')
    group_id = int(request.POST.get('group'))
    user = Athlete.objects.filter(name=name)
    if name is '':
        return render(request, 'draw/info.html', {'text': '姓名不能为空！'})
    if user.exists():
        return render(request, 'draw/info.html', {'text': '该名字已经存在！'})
    else:
        if group_id is 1:
            num = 31
            group_name = 'A'
        elif group_id is 2:
            num = 63
            group_name = 'B'
        elif group_id is 3:
            num = 95
            group_name = 'C'
        elif group_id is 4:
            num = 127
            group_name = 'D'
        else:
            return render(request, 'draw/info.html', {'text': '组别不能为空！'})
        print('num:  ' + str(num))
        users = Athlete.objects.filter(name='', id__lte=num, id__gte=num-31)
        print(users)
        if len(users) is 0:
            return render(request, 'draw/info.html', {'text': group_name + '组已满，请选择其他组别！'})
        user = users[0]
        user.name = name
        user.group = group_id
        print(user)
        user.save()
        return render(request, 'draw/info.html', {'text': '您的编号是：' + str(user.number) + '\n' + '您的组别是：' + group_name})


def _init(request):
    array = []
    for i in range(1, 129):
        array.append(i)
    shuffle(array)
    for i in array:
        user = Athlete(number=i)
        user.save()
