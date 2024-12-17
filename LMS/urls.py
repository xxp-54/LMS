
from django.contrib import admin
from django.urls import path

from web.view.Borrow_Book import borrow_book
from web.view.borrowList import borrowed_books
from web.view.loginOut import loginOut
from web.view.UserRegist import regist
from web.view.return_book import return_book
from web.view.search_books import search_books
from web.view.UserLogin import UserLogin
from web.viewMain import *
from web.view.delete_user import delete_user
from web.view.existing_users import existing_users

urlpatterns = [

    path('', index, name='index'),  # 主页
    path("search_books/", search_books, name='search_books'),
    path('login/', login, name='login'),
    path('loginOut/', loginOut, name='loginOut'),
    path('loginTo/', UserLogin, name='loginTo'),
    # path('register/', register_view, name='register'),
    path('borrow_List/',borrow_List),
    path('user_manage/',user_manage),
    path('registTo/',regist,name = 'registTo'),

    path('borrow_book/', borrow_book, name='borrow_book'),
    path('borrowList/', borrowed_books, name='borrowList'),
    path('return_book/', return_book, name='return_book'),
    path('delete_user/',delete_user,name='delete_user'),
    path('existing_users/',existing_users,name='existing_users'),
]
