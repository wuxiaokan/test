import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='192.168.3.159',
    port=3306,
    user='root',
    passwd='Aa123456',
    db='db_syksc',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()


# 修改
def update(sql):
    cursor.execute(sql)
    connect.commit()


# 查询
def select(sql):
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)
    return data


# 添加
def add(sql):
    cursor.execute(sql)
    connect.commit()


# 删除
def delete(sql):
    cursor.execute(sql)
    connect.commit()


if __name__ == '__main__':
    sql = "select * from t_or_user_address where id='6699584982949699584'"
    select(sql)
