import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from function.userDao.delete_user import deleteUser
from function.userDao.user_online import getOnline

@csrf_exempt  # 防止 CSRF 校验
def delete_user(request):
    if request.method == 'POST':
        try:
            # 获取前端传递的书籍名称
            data = json.loads(request.body)
            username1 = data.get('username')
            print(f'用户为{username1}')
            if not username1:
                return JsonResponse({'status': 'error', 'message': '未找到该用户'})

            username = getOnline()
            if deleteUser(username1):
                return JsonResponse({'status': 'success', 'message': '用户已删除'})
            return JsonResponse({'status': 'false', 'message': '删除用户失败'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': '无效的请求方法'}, status=400)