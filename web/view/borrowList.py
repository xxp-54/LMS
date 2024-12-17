from datetime import timedelta

from django.http import JsonResponse

from function.bookDao.findAllBook import findBorrowBook
from function.userDao.user_online import getOnline


def borrowed_books(request):
    try:
        # 获取当前用户的借书记录
        username = getOnline()
        books = findBorrowBook(username)
        # 将借书记录转化为字典列表
        books_list = [
            {
                'name': book[0],
                'borrow_date': book[2].strftime('%Y-%m-%d'),
                'return_date': (book[2]+timedelta(days=7)).strftime('%Y-%m-%d')
            }
            for book in books
        ]

        # 返回借书记录的 JSON 响应
        return JsonResponse({'books': books_list})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
