
from django.contrib import admin
from django.urls import path

from web.view.loginOut import loginOut
from web.view.UserRegist import regist
from web.view.search_books import search_books
from web.view.UserLogin import UserLogin
from web.viewMain import *

urlpatterns = [

    path('', index, name='index'),  # 主页
    path("search_books/", search_books, name='search_books'),
    path('login/', login, name='login'),
    path('loginOut/', loginOut, name='loginOut'),
    path('loginTo/', UserLogin, name='loginTo'),
    # path('register/', register_view, name='register'),
    path('borrow_return',borrow_return),
    path('return_',return_),
    path('borrow',borrow),
    path('registTo/',regist,name = 'registTo')
]
