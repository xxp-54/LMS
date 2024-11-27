from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def borrow_book(request):
    if request.method == 'POST':
        # 获取前端传过来的书籍ID和用户名（假设前端发送的是书籍ID和当前用户名）
        book_id = request.POST.get('book_id')
        username = request.POST.get('username')

        # 获取对应的书籍和用户对象
        book = get_object_or_404(Book, id=book_id)
        user = get_object_or_404(User, username=username)

        # 检查书籍是否可借
        if book.available:
            # 创建借阅记录
            borrow = Borrow(book=book, user=user)
            borrow.save()

            # 更新书籍的可借状态
            book.available = False  # 借出后，书籍不可借
            book.save()

            # 返回借书成功的消息
            return JsonResponse({
                'status': 'success',
                'message': '借书成功',
                'username': user.username,
                'book_name': book.name
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': '该书已借出，暂时不可借阅'
            })

    return JsonResponse({
        'status': 'error',
        'message': '无效的请求'
    })