from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import records
from .forms import Createrecord
from django.http import JsonResponse
from django.db.models import Sum, Max, Min
# Create your views here.


def index(request):
    record = records.objects.all()
    # aggregate方法計算times欄位的總次數
    sum_times = records.objects.aggregate(Sum('times'))['times__sum']
    max_times = records.objects.all().aggregate(Max('times'))['times__max']
    max_objects = records.objects.filter(times=max_times)
    max_kings_values = [obj.kings for obj in max_objects]
    min_times = records.objects.all().aggregate(Min('times'))['times__min']
    total = records.objects.count()  # 總共有多少紀錄

    # 表單
    form = Createrecord()
    if request.method == "POST":
        form = Createrecord(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/#")

    my_data = {
        "record": record, "form": form,
        "sum_times": sum_times, "total": total,
        "max_times": max_times, "min_times": min_times,
        "max_kings_values": max_kings_values,
    }
    return render(request, 'index.html', my_data)


def update(request, id):
    record = records.objects.get(id=id)
    return render(request, 'update.html', {"record": record})


def updaterecord(request, id):  # 修改
    x = request.POST['kings']
    y = request.POST['times']
    record = records.objects.get(id=id)
    record.kings = x
    record.times = y
    record.save()
    return redirect(('index'))


def add(request):
    return render(request, 'add.html')


def addrecord(request):  # 新增
    x = request.POST['king']
    y = request.POST['times']
    members = records(kings=x, times=y)
    members.save()
    return redirect('index')


def delete(request, id):  # 刪除
    record = records.objects.get(id=id)
    record.delete()
    return redirect('/')


def jsondata(request):
    datas = list(records.objects.values())
    kings = []
    times = []
    for i in range(len(datas)):
        kings.append(datas[i]["kings"])
    for x in range(len(datas)):
        times.append(datas[x]["times"])
    return JsonResponse({'kings': kings, 'times': times})
    '''
    for i in range(len(data)):
        print(data[i]["kings"])
    return JsonResponse(data, safe=False)
    '''
