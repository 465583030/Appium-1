# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.public.空间 import *


# 空间
@ddt.ddt
class Space:
    def __init__(self):
        # 1.创建数据库操作对象
        self.d = DataMysql()
        # 2.创建读取配置信息对象
        self.cf = GlobalParam('config', 'path_file.conf')
        # 3.获取截图路径、日志路径、日志名
        self.logfile = self.cf.getParam('log', "logfile")  # 日志文件名
        # 4.url
        self.url = self.cf.getURL('space', "url")  # url
        # 5.创建日志记录模块
        self.log = Log(self.logfile)
        # 6.获取token
        # self.t = GetToken()
        self.token = self.cf.getToken('token', 'token')

    # 2.创建空间
    def createspace(self, sql, d_index):
        '''创建空间
        :param sql: sql查询语句
        :param d_index: 数据索引
        :return:
        '''
        # 0.获取token
        '''
        ********************下面两行临时注释 ********************
        '''
        # self.log.info('**获取token值：')
        # self.token = self.t.get_token()
        # 0.拼接url
        url_createspace = self.cf.getURL('space', 'createspace')
        url = self.url + url_createspace
        self.log.info('**请求url：{0}'.format(url))
        self.log.info('**请求方法:post')
        # 1. 创建请求对象
        r = RequestForHttp()
        # 2.组装数据-[{...},{...}...]对象 列表-字典
        data = self.d.data_assembly(sql)
        data = data[d_index]
        # 3. 组装token和data
        '''
        ********************临时调试用：token ********************
        '''
        data['token'] = self.token
        self.log.info('**body参数：{0}'.format(data))
        # 4. 发送请求
        response = r.post_function(url, data)
        self.log.info('**响应结果：{0}'.format(response[1]))
        return response

    # 2.关闭空间
    def closespace(self, organization_id):
        '''关闭空间
        :param sql: sql查询语句
        :param d_index: 数据索引
        :return:
        '''
        # 0.获取token
        '''
        ********************下面两行临时注释 ********************
        '''
        # self.log.info('**获取token值：')
        # self.token = self.t.get_token()
        self.log.info('**请求url：{0}'.format(self.url))
        self.log.info('**请求方法:post')
        # 1. 创建请求对象
        r = RequestForHttp()
        # 2.组装url
        url_closespace = self.cf.getURL('space', 'closespace')
        # organization_id = self.d.select(sql)  # 二元列表
        # organization_id = organization_id[0][0]
        part_url = '/%s/organization' % organization_id
        url = self.url + url_closespace + part_url
        # print('url = ', url)
        self.log.info('**拼接后url：{0}'.format(url))
        # 3. 组装token和data
        '''
        ********************临时调试用：token ********************
        '''
        # 创建data字典
        key = 'token'
        data = {key: self.token}
        self.log.info('**body参数：{0}'.format(data))
        # 4. 发送请求
        response = r.delete_function(url, data)
        self.log.info('**响应结果：{0}'.format(response[1]))
        return response

    # 空间列表
    def spaces_list(self, page=None, q=None, class1=None, stranger_id=None):
        '''
        空间列表
        :param q:
        :param class1:
        :param stranger_id:
        :return:
        '''
        # 0.获取token
        '''
        ********************下面两行临时注释 ********************
        '''
        # self.log.info('**获取token值：')
        # self.token = self.t.get_token()
        self.log.info('**请求url：{0}'.format(self.url))
        self.log.info('**请求方法:post')
        # 1. 创建请求对象
        r = RequestForHttp()
        # 2.组装url
        url_spaces_list = self.url + self.cf.getURL('space', 'spaces_list')
        self.log.info('**拼接后url：{0}'.format(url_spaces_list))
        # 3. 组装token和data
        '''
        ********************临时调试用：token ********************
        '''
        # 创建data字典
        key = 'token'
        data = {key: self.token}
        self.log.info('**body参数：{0}'.format(data))
        # 4. 发送请求
        response = r.get_function(url_spaces_list, data)
        self.log.info('**响应结果：{0}'.format(response[1]))
        return response


l = Space()
#
# sql = 'select * from test1_1_space_01'
# l.createspace(sql, 0)
#
# sql = 'select * from test1_1_closespace_01'
# l.closespace('5789')
l.spaces_list()
