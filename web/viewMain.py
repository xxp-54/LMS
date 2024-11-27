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
    return render(request, 'index.html', {'user': user})  # 渲染 index.html 模板

#登录页面
def login(request):
    return render(request,'login_new.html')

def borrow_return(request):
    return render(request,'borrow_return.html')

def borrow(request):
    return render(request,'borrow.html')

def return_(request):
    return render(request,'return.html')



# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             userDao = authenticate(username=username, password=password)
#             if userDao is not None:
#                 auth_login(request, userDao)
#                 return redirect('home')  # 重定向到首页
#             else:
#                 form.add_error(None, '用户名或密码错误')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login_new.html', {'form': form})
#
# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # 可以在这里添加登录逻辑
#             return redirect('login')  # 注册后重定向到登录页面
#     else:
#         form = UserCreationForm()
#     return render(request, 'login_new.html', {'form': form})

