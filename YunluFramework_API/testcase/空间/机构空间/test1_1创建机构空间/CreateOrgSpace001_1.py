__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.testcase.空间.机构空间.test1_1创建机构空间 import *


# 空间
@ddt.ddt
class SpaceAPI(unittest.TestCase):
    d = DataMysql()
    sql = 'select * from test1_1_space_01'

    # 1.初始化
    def setUp(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志记录模块
        self.log = Log(self.logfile)
        # 4.打印日志
        self.log.info('创建空间接口：开始')
        self.log.info("------------START:test1_1创建空间.CreateOrgSpace001_1.py------------")
        self.log.info('**接口描述：创建空间接口')
        # 5.创建登录对象
        self.S = Space()

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test1_1创建空间.CreateOrgSpace001_1.py------------")
        self.log.info('创建空间接口：结束\n')
        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    @ddt.data([sql, 0])
    @ddt.unpack
    def test_createspace01(self, sql, d_index):
        '''创建机构空间-正确流程
        :param sql: sql语句
        :param d_index: 数据索引1
        :return:
        '''
        try:
            # 1. 调用登录请求
            response = self.S.createspace(sql, d_index)
            # 1.1.更新数据库
            organization_id = json.loads(response[1])['organization_id']
            self.d.update(organization_id)
            self.log.info('更新数据库organization_id：{0}'.format(organization_id))
            # 2. 解析数据，断言
            # 2.1状态码
            self.log.info('1.判断返回状态码：{0} = {1}'.format(201, response[0]))
            assert 201 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')
            # 2.2返回数据
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} = {1}'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')
        except Exception as err:
            self.log.error("Login Outside : %s" % err)
            raise err

    @ddt.data([sql, 1])
    @ddt.unpack
    def test_createspace02(self, sql, d_index):
        '''创建机构空间-错误流程1：简称重复
        :param sql: sql语句
        :param d_index: 数据索引1
        :return:
        '''
        try:
            # 1. 调用登录请求
            response = self.S.createspace(sql, d_index)
            # 2. 解析数据，断言
            # 2.1状态码
            self.log.info('1.判断返回状态码：{0} = {1}'.format(201, response[0]))
            assert 201 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')
            # 2.2返回数据
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} = {1}'.format('True', response['success']))
            assert False == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')
        except Exception as err:
            self.log.error("Login Outside : %s" % err)
            raise err
    #
    # @ddt.data([sql, 2])
    # @ddt.unpack
    # def test_login03(self, sql, d_index):
    #     '''登录-错误流程2
    #     :param sql: sql语句
    #     :param d_index: 数据索引2
    #     :return:
    #     '''
    #     try:
    #         # 1. 调用登录请求
    #         response = self.L.loginRequest(sql, d_index)
    #         # 2. 解析数据，断言
    #         # 2.1状态码
    #         self.log.info('1.判断返回状态码：{0} = {1}'.format(401, response[0]))
    #         assert 401 == response[0], '返回状态不正确：{0}'.format(response[0])
    #         self.log.info('status_code：OK')
    #         # 2.2返回数据
    #         response = json.loads(response[1])
    #         self.log.info(
    #             '2.判断error：{0} = {1}'.format('401 Unauthorized', response['error']))
    #         assert '401 Unauthorized' == response['error'], 'device_id返回不正确：{0}'.format(
    #             response['device_id'])
    #         self.log.info('device_id：OK')
    #     except Exception as err:
    #         self.log.error("Login Outside : %s" % err)
    #         raise err
