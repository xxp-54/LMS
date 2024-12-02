from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from function.bookDao.borrowBook import addBorrowedBook
from function.userDao.user_online import getOnline


@csrf_exempt
def borrow_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            book_name = data.get('name')

            user = getOnline()
            if user is None:
                return JsonResponse({'status': 'fail', 'message': '用户未登录'}, status=403)
            addBorrowedBook(book_name,user)

            return JsonResponse({'status': 'success', 'message': f'已成功借阅《{book_name}》'})
        except Exception as e:
            return JsonResponse({'status': 'fail', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'fail', 'message': '仅支持 POST 请求'}, status=405)
