from django.http import JsonResponse

from function.bookDao.findAllBook import findAllBook
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from function.userDao.user_online import getOnline
from .form import CustomAuthForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



def index(request):
    user = getOnline()
    return render(request, 'index.html', {'user': user, 'message': ''})  # 渲染 index.html 模板

#登录页面
def login(request):
    return render(request,'login_new.html')

def borrow_List(request):
    user = getOnline()
    return render(request, 'borrowList.html', {'user': user})


def return_(request):
    return render(request,'return.html')


def user_manage(request):
    user = getOnline()
    if user!='root':
        return render(request, 'index.html', {'user': user,'message': '用户权限不够'})
    return render(request,'user_manage.html',{'user': user, 'message': ''})


