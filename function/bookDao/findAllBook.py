from function.select.jdbc import execute_query

def findAllBook():
    query = "SELECT Book_name,Book_writer FROM t_book "
    results = execute_query(query)
    if results is not None:
        return results
    else:
        return None


