from django.shortcuts import render, redirect
from .forms import myuserform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def user_register(request):
    message = ''
    if request.method == "POST":
        form = myuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        else:
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')
            if len(password1) < 8:
                message = '密碼少於8個字元'

            elif password1 != password2:
                message = '兩次密碼不相同'
            else:
                if User.objects.filter(username=username).exists():
                    message = '帳號重複'

    else:
        form = myuserform()
    return render(request, "register.html", {"form": form, "message": message})


def user_login(request):
    username, message = '', ''
    if request.method == 'POST':
        if request.POST.get('login'):  # 按下登入按鈕
            username = request.POST.get('username')
            password = request.POST.get('password')
            # 檢查帳號密碼是否為空
            if username == '' or password == '':
                message = '帳號跟密碼不能為空'
            else:
                # 檢查資料庫是否有該使用者
                # 匹配密碼進行登入
                user = authenticate(
                    request, username=username, password=password)
                if user is None:
                    if User.objects.filter(username=username):
                        message = '密碼有誤'
                    else:
                        message = '帳號有誤'
                else:
                    login(request, user)
                    message = '登入中'
                    return redirect('index')
        elif request.POST.get('signup'):
            return redirect('signup')
    return render(request, 'login.html', {'message': message, 'username': username})
