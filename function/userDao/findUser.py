from function.select.jdbc import execute_query, execute_query_with_params


def findAllUser():
    query = "SELECT *  FROM user"
    results = execute_query(query)
    if results is not None:
        return results
    else:
        return None

def findUser(username):
    query = "SELECT * FROM user WHERE user_name = %s"
    params = (username,)
    results = execute_query_with_params(query, params)
    if results:
        return results[0]
    else:
        return None