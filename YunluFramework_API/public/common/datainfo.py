import xlrd
import os
import mysql.connector
from YunluFramework_API.config.globalparam import GlobalParam
import configparser
import xlwt


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

    # --------------------------------------------Excel表格读取操作--------------------------------------------
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


class DataWrite():
    def __init__(self, filename):
        self.filename = filename

    # --------------------------------------------Excel表格写入操作--------------------------------------------
    def write_data(self, fields, result):
        workbook_new = xlwt.Workbook()
        sheet_new = workbook_new.add_sheet('login', cell_overwrite_ok=True)

        # 第一行的数据（字段）：列表
        # fields_1 = a.get_Fields(sql)
        for i in range(0, len(fields)):
            sheet_new.write(0, i, '%s' % fields[i])

        # 第n行数据（测试数据）：列表
        # list_result = a.select(sql)
        for i in range(0, len(result)):
            for j in range(0, len(result[i])):
                sheet_new.write(i + 1, j, '%s' % result[i][j])

        workbook_new.save(self.filename)


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
        # 6.关闭游标
        cursor.close()
        cnn.close()
        return fields

    # 执行查询语句，返回列表
    def select(self, sql):
        '''
        数据库查询
        :param sql: 查询语句
        :param index:查询结果索引
        :return:查询结果列表（双层）
        例如：[
        ['13027104206', '1234567', 'KNT-AL20', '862537039675333', 'andriod'],
        ['13027104206', '12345678', 'KNT-AL20', '862537039675333', 'andriod']
        ]
        '''
        # 1.申请连接对象
        cnn = self.connect()
        # 2.创建游标
        cursor = cnn.cursor()
        # 3.利用游标执行查询语句
        cursor.execute(sql)
        # 4.记录结果
        # 4.1 查询结果
        result = cursor.fetchall()
        # 4.2 将结果存到列表中去
        list_result = []
        for i in range(0, len(result)):
            list_result.append(list(result[i]))
        # 5.关闭游标
        cursor.close()
        cnn.close()
        return list_result

    # 数据组装
    def data_assembly(self, sql):
        '''
        数据组装
        :return: 返回字典数据
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

        # 6.记录结果
        # 6.1 查询结果
        result = cursor.fetchall()

        # 7. 组装
        # 7.1查询结果-列表[][]
        list_result = []
        for i in range(0, len(result)):
            list_result.append(list(result[i]))

        # 8.1空列表，存字典
        dict_list = []
        # 8.2组装数据
        for i in range(0, len(result)):
            dictionary1 = dict(zip(fields, result[i]))
            dict_list.append(dictionary1)

        cursor.close()
        cnn.close()
        return dict_list

    # 插入数据
    def insert(self, *args, **kwargs):
        '''
        插入数据
        :param sql:
        :return:
        '''
        try:
            # 1.申请连接对象
            cnn = self.connect()
            # 2.创建游标
            cursor = cnn.cursor()
            # 3.元祖连接插入方式
            sql_insert2 = "insert into test1_1_closespace_01(organization_id) values (%s)"
            # 此处的%s为占位符，而不是格式化字符串，所以age用%s，占用一个位置，后期可以直接替换参数，比较常用
            data = (args)
            cursor.execute(sql_insert2, data)
            cnn.commit()
        except mysql.connector.Error as e:
            print('insert data error!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()

    # 更新数据
    def update(self, *args, **kwargs):
        '''
        插入数据
        :param sql:
        :return:
        '''
        try:
            # 1.申请连接对象
            cnn = self.connect()
            # 2.创建游标
            cursor = cnn.cursor()
            # 3.元祖连接插入方式
            # sql_insert2 = "insert into test1_1_closespace_01(organization_id) values (%s)"
            sql_update = 'UPDATE test1_1_closespace_01 SET organization_id = %s'%args
            # 此处的%s为占位符，而不是格式化字符串，所以age用%s，占用一个位置，后期可以直接替换参数，比较常用
            cursor.execute(sql_update)
            cnn.commit()
        except mysql.connector.Error as e:
            print('update data error!{}'.format(e))
        finally:
            cursor.close()
            cnn.close()
# #
# # ----------测试-----------
# # 1.查询数据
# a = DataMysql()
# sql = 'select * from test1_1_login_01'
# print(a.data_assembly(sql))
#
# # 2.组装数据-[{...},{...}...]对象 列表-字典
# data = a.data_assembly(sql)
#
# import requests
# import json
#
# url = 'https://api.yunlu6.com/api/v1/login'
# # 3.发送请求
# r = requests.post(url, data=data[1])
#
# # 4.打印请求状态码
# # print(r.status_code)
# response = r.text
#
# # 5.解码json数据,将json转为字典
# dict_r = json.loads(response)
#
# # 6.格式化输出json
# # ensure_ascii=False 中文不转码
# json_r = json.dumps(dict_r, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
# print(json_r)
#
# # 7. 将测试数据写入excel文档中
# # 文件名
# filename = '../../data/data.xls'
# # 第一行的数据（字段）：列表
# fields_1 = a.get_Fields(sql)
# # 第n行数据（测试数据）：列表
# list_result = a.select(sql)
# d = DataWrite(filename)
# d.write_data(fields_1, list_result)

# a = DataMysql()
# a.insert('5761')
# a.update('8888')
# a.insert(5761)
