from function.utils.jdbc import execute_query, execute_query_with_params


def findAllBook(search):
    query = "SELECT bname,author FROM t_book where bname like %s"
    params = ("%"+search+"%",)
    rows_affected = execute_query_with_params(query, params)
    if rows_affected is not None:
        return rows_affected
    else:
        return []


def findBorrowBook(username):
    query = "SELECT * FROM borrowed_books where username like %s "
    params = (username,)
    results = execute_query_with_params(query, params)
    if results is not None:
        return results
    else:
        return []



