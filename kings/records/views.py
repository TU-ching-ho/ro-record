from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import records
from .forms import Createrecord
from django.http import JsonResponse
from django.db.models import Sum, Max, Min
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, "home.html")


@login_required
def index(request):
    record = records.objects.filter(user=request.user)
    # aggregate方法計算times欄位的總次數
    sum_times = records.objects.filter(
        user=request.user).aggregate(Sum('times'))['times__sum']
    total = records.objects.filter(user=request.user).count()  # 總共有多少紀錄
    order_record = records.objects.filter(
        user=request.user).order_by("-times")  # 排序
    #max_times = records.objects.all().aggregate(Max('times'))['times__max']
    #max_objects = records.objects.filter(times=max_times)
    #max_kings_values = [obj.kings for obj in max_objects]
    #min_times = records.objects.all().aggregate(Min('times'))['times__min']

    # 表單
    form = Createrecord()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = Createrecord(request.POST)
            if form.is_valid():
                kings = form.cleaned_data.get('kings')
                if records.objects.filter(kings=kings, user=request.user).exists():
                    return HttpResponse("Error: kings value already exists")
                else:
                    # Commit to False to prevent saving to DB immediately
                    record = form.save(commit=False)
                    record.user = request.user  # Set the user field to the currently authenticated user
                    record.save()  # Save the record with the user information
                return redirect("/views")
        else:
            return redirect('login')

    my_data = {
        "record": record, "form": form,
        "sum_times": sum_times, "total": total,
        "order_record": order_record,
    }
    return render(request, 'index.html', my_data)


@login_required
def update(request, id):
    record = records.objects.get(id=id)
    return render(request, 'update.html', {"record": record})


@login_required
def updaterecord(request, id):  # 修改
    x = request.POST['kings']
    y = request.POST['times']
    record = records.objects.get(id=id)
    record.kings = x
    record.times = y
    record.save()
    return redirect(('index'))


@login_required
def add(request):
    return render(request, 'add.html')


@login_required
def addrecord(request):  # 新增
    x = request.POST['king']
    y = request.POST['times']
    members = records(kings=x, times=y)
    members.save()
    return redirect('index')


@login_required
def delete(request, id):  # 刪除
    record = records.objects.get(id=id)
    record.delete()
    return redirect('index')


@login_required
def jsondata(request):
    record = records.objects.filter(user=request.user)
    datas = list(record.values())
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
