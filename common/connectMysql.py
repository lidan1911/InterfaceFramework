import pymysql


class ConnectMysql:
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(host='192.168.100.55',
                             port=3306,
                             user='root',
                             passwd='root',
                             db='db_school',
                             charset='utf8')  # 避免查询结果乱码
        # 使用cursor()方法创建一个游标对象cur
        self.cur = self.db.cursor()

    def query(self, sql):
        '''
        通过sql语句查询数据
        :param sql: sql查询语句
        :return: data->查询结果
        '''
        self.cur.execute(sql)
        # 使用fetchall()方法获取查询结果
        data = self.cur.fetchall()
        return data
        self.db.close()

    def notQuery(self, sql):
        '''
        通过sql语句执行增删改操作
        :param sql: 增删改sql
        :return:
        '''
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print("错误信息：%s" % str(e))
            self.db.rollback()
        finally:
            self.db.close()

if __name__ == '__main__':
    data = ConnectMysql().query("select * from student")
    print(data)




