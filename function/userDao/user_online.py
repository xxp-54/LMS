from function.utils.jdbc import execute_query_with_params


def user_Online(username):
    query = "INSERT INTO user_online (user_name) VALUES (%s)"
    params = (username,)
    rows_affected = execute_query_with_params(query, params)
    if rows_affected is not None and rows_affected > 0:
        print(f"成功更新了 {rows_affected} 行。")
    else:
        print("更新失败或未找到匹配记录。")

def user_Outline():
    query = "DELETE from user_online"
    params = ()
    rows_affected = execute_query_with_params(query, params)
    if rows_affected is not None and rows_affected > 0:
        print(f"成功更新了 {rows_affected} 行。")
    else:
        print("更新失败或未找到匹配记录。")


def getOnline():
    query = "SELECT * FROM user_online"
    params = ()
    result = execute_query_with_params(query, params)

    if result is not None and len(result) > 0:
        # 确保返回结果的第一行第一列
        return result[0][0]
    else:
        # 返回 None 表示没有数据
        return []