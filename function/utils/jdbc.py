import mysql.connector
from mysql.connector import Error

def execute_query(query):
    """
    执行不带参数的 MySQL 查询并返回结果。

    参数:
        query (str): 要执行的查询语句。

    返回:
        list: 查询结果（元组的列表）。
        None: 如果出现错误。
    """
    try:
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='library'
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                return results
    except Error as err:
        print(f"Error executing query: {query}\nError: {err}")
        return None


def execute_query_with_params(query, params):
    try:
        print(f"Executing query: {query} with params: {params}")  # 调试信息
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='library'
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)

                # 检查查询类型
                if query.strip().lower().startswith("select"):
                    results = cursor.fetchall()
                    print(f"Query results: {results}")  # 打印查询结果
                    return results
                else:
                    # 提交事务并返回受影响行数
                    conn.commit()
                    print(f"Rows affected: {cursor.rowcount}")  # 打印受影响的行数
                    return cursor.rowcount
    except Error as err:
        print(f"Error executing query: {query} with params: {params}\nError: {err}")
        return None
