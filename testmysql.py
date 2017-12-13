import mysql.connector  # 引入需要导入的包

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'port': '3306',
    'database': 'YunluFramework',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
    print('mysql连接对象是cnn', cnn)
except mysql.connector.Error as e:
    print('connect fails!{0}'.format(e))

print('==============查询表==============')
cursor = cnn.cursor()  # 创建游标
sql_select_table = "select * from test1_1创建机构空间_002"
cursor.execute(sql_select_table)
# print(cursor.fetchone())
result = cursor.fetchall()
print(result[0])

print('==============插入数据==============')
cursor = cnn.cursor()  # 创建游标
sql_select_table = "select * from test1_1创建机构空间_002"
cursor.execute(sql_select_table)
# print(cursor.fetchone())
result = cursor.fetchall()
print(result[0])

#-----------------------------------------------------------------------------------------------------------------------
import xlrd
path = "/Users/xiaojingyuan/PycharmProjects/Appium/YunluFramework/data/space.xls"
workbook = xlrd.open_workbook(path)
sheet_obj = workbook.sheet_by_index(0)
print(sheet_obj.row_values(0))