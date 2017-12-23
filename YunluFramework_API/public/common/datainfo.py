import xlrd
import os
import mysql.connector
from YunluFramework_API.config.globalparam import GlobalParam
import configparser


class DataInfo():
    def __init__(self, path):
        '''
        :param path: 传入xls文档名称，例如space.xls
        '''
        # 项目目录
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # 数据data目录文件拼接
        base_dir = base_dir + "/data/" + path
        # 创建工作薄：用于操作excel表格形式数据
        self.workbook = xlrd.open_workbook(base_dir)

    # --------------------------------------------Excel表格操作--------------------------------------------
    def read_Data(self, sheet_name):
        '''
        根据表单名来获取表单对象
        :param sheet_name:表单名称
        :return:表单对象
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        return sheet_obj

    def row(self, sheet_name, rowno):
        '''
        改写行，输入1就返回第一行
        :param sheet_name: 表单名
        :param rowno: 行数
        :return:获取第一行的值，列表形式返回['A',"B','C',...]
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        rowno = rowno - 1
        return sheet_obj.row_values(rowno)

    def col(self, sheet_name, colno):
        '''
        改写列，输入1就返回第一列
        :param sheet_name: 表单名
        :param colno:列数
        :return:获取第一列的值，列表形式返回['A',"B','C',...]
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        colno = colno - 1
        return sheet_obj.row_values(colno)

    def cell(self, sheet_name, rowno, colno):
        '''
        改写行列，输入(1,1)就返回(1,1)的数据
        :param sheet_name:表单名
        :param rowno:行数
        :param colno:列数
        :return: 返回某个坐标行列的值
        '''
        sheet_obj = self.workbook.sheet_by_name(sheet_name)
        rowno = rowno - 1
        colno = colno - 1
        return sheet_obj.cell_value(rowno, colno)


class DataMysql:
    def __init__(self):
        # 读取数据库连接信息
        # 1.项目目录
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        # 2.数据库配置文件
        self.config = base_dir + "/config/sqlserver.conf"
        # 3.读取配置信息
        cf = configparser.ConfigParser()
        cf.read(self.config)
        sections_01 = cf.sections()[0]
        self.connectinfo = eval(cf.get(sections_01, "config"))

    # --------------------------------------------数据库操作--------------------------------------------
    # 建立连接
    def connect(self):
        '''
        建立数据库连接
        :return:返回数据库连接对象
        '''
        try:
            cnn = mysql.connector.connect(**self.connectinfo)
            # print('mysql连接对象是cnn', cnn)
            return cnn
        except mysql.connector.Error as e:
            print('CONNECT MYSQL FAILS!:{0}'.format(e))

    # 获取数据库字段名，返回列表
    def get_Fields(self, sql):
        '''
        获取数据库字段名
        :param sql: 查询语句
        :return: 返回字段名列表
        '''
        # 1.申请连接对象
        cnn = self.connect()
        # 2.创建游标
        cursor = cnn.cursor()
        # 3.查询表信息
        cursor.execute(sql)
        # 4.获取描述信息
        desc = cursor.description
        # 5.循环取字段名
        fields = []
        for i in range(0, len(desc)):
            desc_i = desc[i][0]
            fields.append(desc_i)
        return fields

    # 执行查询语句，返回列表
    def select(self, sql, index):
        '''
        数据库查询
        :param sql: 查询语句
        :param index:查询结果索引
        :return:查询结果
        '''
        # 1.申请连接对象
        cnn = self.connect()
        # 2.创建游标
        cursor = cnn.cursor()
        # 3.利用游标执行查询语句
        cursor.execute(sql)
        # sql_select_table = "select * from test1_1创建机构空间_002"
        # print(cursor.fetchone())
        # 4.记录结果
        result = cursor.fetchall()
        return list(result[index])

    # 数据组装
    def data_assembly(self, sql, index):
        '''
        数据组装
        :return: 返回字典数据
        '''
        # 1.声明空字典
        data_assmbly = {}
        # 2. 组装
        # 2.1查询结果
        result = self.select(sql, index)
        # 2.2字段名
        fields = self.get_Fields(sql)
        #3.组装数据
        for i in range(0,len(fields)):
            data_assmbly[fields[i]] = result[i]
        return data_assmbly


# ----------测试-----------


# 1.查询数据
a = DataMysql()
sql = 'select * from test1_1_login_01'

# 2.组装数据
data = a.data_assembly(sql,0)
print(data)
print(type(data))

import requests
import json


url = 'https://api.yunlu6.com/api/v1/login'
# 3.发送请求
r = requests.post(url, data=data)

# 4.打印请求状态吗
# print(r.status_code)
response = r.text

# 5.解码json数据,将json转为字典
dict_r = json.loads(response)
# 获取id，用字典取数据
# print(dict_r['id'])

# 6.格式化输出json
json_r = json.dumps(dict_r, sort_keys=True, indent=4, separators=(',', ': '))
print(json_r)


'''
# 7. 将测试数据写入excel文档中
import xlwt

# 文件名
filename = '../../data/data.xls'

# 原始测试数据
print('原始拼接data:', data)
workbook_new = xlwt.Workbook()
sheet_new = workbook_new.add_sheet('login', cell_overwrite_ok=True)

# 第一行的数据：列表
list_1 = list(data.keys())
print('data字典所有的键:', list_1)

# 循环写第一行数据
for i in range(0, len(data.keys())):
    sheet_new.write(0, i, '%s' % list_1[i])

for i in range(0, len(result)):
    sheet_new.write(1, i, '%s' % result[i])

workbook_new.save(filename)
'''
