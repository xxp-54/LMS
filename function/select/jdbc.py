import mysql.connector
from mysql.connector import Error

def execute_query(query):
    """
    执行 不带参数的MySQL 查询并返回结果的通用函数。

    参数:
        query (str): 要执行的查询语句。

    返回:
        list: 查询结果（元组的列表）。
        None: 如果出现错误。
    """
    try:
        # 连接到 MySQL 数据库
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='library'
        ) as conn:

            # 创建一个游标对象
            cursor = conn.cursor()

            # 执行查询
            cursor.execute(query)

            # 获取所有结果
            results = cursor.fetchall()

            return results
    except Error as err:
        print(f"Error: {err}")
        return None  # 返回 None 以示意出错









def execute_query_with_params(query, params):
    """
    执行带参数的 MySQL 查询。

    参数:
        query (str): 查询语句（SELECT、UPDATE、INSERT 或 DELETE）。
        params (tuple): 查询参数。

    返回:
        list: 如果是查询操作 (SELECT)，返回查询结果（元组的列表）。
        int: 如果是修改操作 (UPDATE/INSERT/DELETE)，返回受影响的行数。
        None: 如果发生错误。
    """
    try:
        # 连接到 MySQL 数据库
        with mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456',
            database='library'
        ) as conn:
            cursor = conn.cursor()

            # 执行查询
            cursor.execute(query, params)

            if query.strip().lower().startswith("select"):
                # 如果是查询操作，返回结果
                results = cursor.fetchall()
                return results
            else:
                # 如果是修改操作，提交事务并返回受影响的行数
                conn.commit()
                return cursor.rowcount
    except Error as err:
        print(f"Error: {err}")
        return None


