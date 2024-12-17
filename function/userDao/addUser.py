from function.utils.jdbc import execute_query_with_params


def addUser(username,password):
    query = "insert into user (user_name,password) values (%s,%s)"
    params = (username,password)
    rows_affected = execute_query_with_params(query, params)
    if rows_affected is not None and rows_affected > 0:
        print(f"成功插入了 {rows_affected} 行。")
    else:
        print("更新失败或未找到匹配记录。")