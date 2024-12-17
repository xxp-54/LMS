from datetime import timedelta

from django.http import JsonResponse

from function.userDao.findUser import findAllUser
from function.userDao.user_online import getOnline


def existing_users(request):
    try:
        users = findAllUser()
        user_list = [
            {
                'id': user[0],
                'user_name': user[1],
            }
            for user in users
        ]
        return JsonResponse({'users': user_list})


    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
