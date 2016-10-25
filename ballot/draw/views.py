from django.shortcuts import render
from .models import Athlete
from random import shuffle, randrange
from django.http import HttpResponse
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
        users = Athlete.objects.filter(name='', number__lte=num, number__gte=num-31)
        if len(users) is 0:
            return render(request, 'draw/info.html', {'text': group_name + '组已满，请选择其他组别！'})
        user = users[randrange(0, len(users))]
        user.name = name
        user.group = group_id
        user.save()
        return render(request, 'draw/info.html', {'text': '您的编号是：' + str(user.number) + '\n' + '您的组别是：' + group_name})


def init(request):
    array = []
    for i in range(1, 129):
        array.append(i)
    shuffle(array)
    for i in array:
        user = Athlete(number=i)
        user.save()
    return HttpResponse('初始化完毕。')
