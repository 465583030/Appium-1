# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.public.登陆 import *


# 登录
@ddt.ddt
class Login:

    def __init__(self):
        # 1.创建数据库操作对象
        self.d = DataMysql()
        # 2.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 3.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 4.url
        self.url = cf.getURL('login', "url")  # 日志文件名
        # 5.创建日志记录模块
        self.log = Log(self.logfile)

    # 2.发送请求
    def loginRequest(self, sql, d_index):
        '''发送登录请求
        :param sql: sql查询语句
        :param d_index: 数据索引
        :param r_index: 返回值索引
        :return:
        '''
        self.log.info('2、请求url：{0}'.format(self.url))
        self.log.info('3、请求方法:post')
        # 1. 创建请求对象
        r = RequestForHttp()
        # 2.组装数据-[{...},{...}...]对象 列表-字典
        data = self.d.data_assembly(sql)
        data = data[d_index]
        self.log.info('4、body参数：{0}'.format(data))
        # 3. 发送请求
        response = r.post_function(self.url, data)
        self.log.info('5、响应结果：{0}'.format(response[1]))
        return response
