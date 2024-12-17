

from function.utils.jdbc import execute_query_with_params

def deleteUser(username):
    query = "DELETE from user WHERE  user_name = %s"
    params = (username,)
    try:
        # Execute the query and get the number of rows affected
        rows_affected = execute_query_with_params(query, params)
        if rows_affected is not None and rows_affected > 0:
            return True
        else:
            return False

    except Exception as e:
        # Log or print the exception if needed
        print(f"Error deleting borrowed book: {e}")
        return False
