from function.utils.jdbc import execute_query_with_params


def addBorrowedBook(bname, username):

    query = "INSERT INTO borrowed_books (bname, username) VALUES (%s, %s)"
    params = (bname, username)
    rows_affected = execute_query_with_params(query, params)
    if rows_affected is not None and rows_affected > 0:
        print(f"成功插入了 {rows_affected} 行借书记录。")
    else:
        print("插入借书记录失败。")
