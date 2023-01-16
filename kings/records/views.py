from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import records
from .forms import Createrecord
# Create your views here.


def index(request):
    record = records.objects.all()
    form = Createrecord()
    if request.method == "POST":
        form = Createrecord(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/#")
    return render(request, 'index.html', {"record": record, "form": form})


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


def delete(request, id):
    record = records.objects.get(id=id)
    record.delete()
    return redirect('/')
