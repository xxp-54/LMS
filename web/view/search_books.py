from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from function.bookDao.findAllBook import findAllBook

@csrf_exempt  # 如果需要允许跨站请求，可以使用这个装饰器
def search_books(request):
    if request.method == 'POST':
        try:
            # 获取请求体中的 JSON 数据
            data = json.loads(request.body)
            book_name = data.get('name', '')  # 获取书名字段
            # 调用数据库查询函数（需要根据实际情况修改）
            results = findAllBook(book_name)

            # 处理查询结果
            if results:
                book_info_list = []
                for result in results:
                    book_info_list.append({
                        'name': result[0],
                        'author': result[1]
                    })
                # 返回 JSON 格式的数据
                return JsonResponse({'results': book_info_list})
            else:
                # 如果没有找到任何结果
                return JsonResponse({'results': []})

        except json.JSONDecodeError:
            # 处理无效的 JSON 请求
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            # 捕获其他异常并返回错误信息
            return JsonResponse({'error': str(e)}, status=500)

    # 如果请求方法不是 POST，返回错误信息
    return JsonResponse({'error': 'Invalid request method'}, status=405)
