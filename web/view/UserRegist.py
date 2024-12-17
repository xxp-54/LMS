import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from function.userDao.addUser import addUser
from function.userDao.findUser import findUser
from function.userDao.user_online import user_Online, getOnline


@csrf_exempt
def regist(request):
    if request.method == 'POST':
        try:
            # 解析 JSON 数据
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            result = findUser(username)
            # 验证用户名和密码（这里是示例，实际情况应查询数据库）
            if result is None :
                addUser(username,password)
                return JsonResponse({'success': True, 'message': '注册成功！'})
            else:
                return JsonResponse({'success': False, 'message': '用户已存在！'})



        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': '无效的 JSON 数据'}, status=400)

        # 如果不是 POST 请求
    return JsonResponse({'success': False, 'message': '只支持 POST 请求'}, status=405)