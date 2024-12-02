import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from function.userDao.findUser import findUser
from function.userDao.user_online import user_Online, getOnline


@csrf_exempt
def UserLogin(request):
    if request.method == 'POST':
        try:
            # 解析 JSON 数据
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            result = findUser(username)
            # 验证用户名和密码（这里是示例，实际情况应查询数据库）
            if password == result[2]:

                user = getOnline()
                if user == []:
                    user_Online(username)
                    return JsonResponse({'success': True, 'message': '登录成功！'})
                return JsonResponse({'success': False, 'message': '用户已经登录！'})
            elif result is None:
                return JsonResponse({'success': False, 'message': '没有此用户！'})
            else:
                return JsonResponse({'success': False, 'message': '账号或密码错误！'})



        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': '无效的 JSON 数据'}, status=400)

        # 如果不是 POST 请求
    return JsonResponse({'success': False, 'message': '只支持 POST 请求'}, status=405)