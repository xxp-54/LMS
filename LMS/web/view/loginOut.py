from django.shortcuts import render

from function.userDao.user_online import user_Outline


def loginOut(request):
    user_Outline()
    return render(request,'login_new.html')