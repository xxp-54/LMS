from django.http import JsonResponse

from function.bookDao.findAllBook import findAllBook


def search_books(request):
    if request.method == 'GET':
        results = findAllBook()  # 调用搜索函数
        print(results)

        book_info_list = []  # 用于存储多个书籍的信息

        for result in results:
            book_info_list.append({
                'name': result[0],
                'author': result[1]
            })

        # 打印所有书籍信息
        print(book_info_list)
        response_data = {'results': book_info_list}  # 格式化为字典，包含书籍列表

        return JsonResponse(response_data)  # 返回 JSON 响应