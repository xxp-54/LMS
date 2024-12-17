import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from function.bookDao.deleteBook import deleteBorrowBook
from function.bookDao.findAllBook import findBorrowBook
from function.userDao.user_online import getOnline




@csrf_exempt  # 防止 CSRF 校验
def return_book(request):
    if request.method == 'POST':
        try:
            # 获取前端传递的书籍名称
            data = json.loads(request.body)
            book_name = data.get('book_name')

            if book_name == []:
                return JsonResponse({'status': 'error', 'message': '未找到该书籍'})

            username = getOnline()
            # 删除借书记录或设置为归还状态
            if deleteBorrowBook(username,book_name):
                return JsonResponse({'status': 'success', 'message': '书籍已归还'})
            return JsonResponse({'status': 'false', 'message': '书籍归还失败'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': '无效的请求方法'}, status=400)
