__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.testcase.空间.机构空间.test1_1创建机构空间 import *
import json


# 空间
@ddt.ddt
class SpaceAPI(unittest.TestCase):
    d = DataMysql()
    sql01 = 'select * from test_SpaceAPI_01'
    sql03 = 'select * from test_SpaceAPI_02'

    # 1.初始化
    def setUp(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 3.创建日志记录模块
        self.log = Log(self.logfile)

        # 4.打印日志
        self.log.info('****************************************创建空间接口：开始****************************************')
        self.log.info("------------START:test1_1创建空间.CreateOrgSpace001_1.py------------")

        # 5.创建登录对象
        self.S = Space()

    # 3.释放资源
    def tearDown(self):
        # 1.打印日志
        self.log.info("------------END:test1_1创建空间.CreateOrgSpace001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~创建空间接口：结束~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    # 4.测试用例
    @ddt.data([sql01, 0])
    @ddt.unpack
    def test_SpaceAPI_01(self, sql, d_index):
        '''创建机构空间
        :param sql: sql语句
        :param d_index: 数据索引1
        :return:
        '''
        try:
            # 1. 调用创建请求
            response = self.S.Space_org_create_api(sql, d_index)
            # 1.1.更新数据库
            organization_id = json.loads(response[1])['organization_id']
            sql = 'UPDATE test_SpaceAPI_02 SET organization_id = %s' % organization_id
            self.d.update(sql)

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
            self.log.error("test_SpaceAPI_01 : %s" % err)
            raise err

    def test_SpaceAPI_02(self):
        '''访问空间列表'''
        try:
            # 1.调用空间列表接口
            response = self.S.Space_list_api()

            # 2.解析数据，断言
            # 2.1 状态码
            self.log.info('1.判断返回状态码：{0} = {1}'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 2.2 遍历结果，检查是否创建成功
            re = json.loads(response[1])
            for r in re:
                if r["company"] == '测试空间123':
                    self.log.info('2.遍历结果，结果中包含创建的空间:{0}'.format(r['company']))
                    break

        except Exception as err:
            self.log.error("test_SpaceAPI_02 : %s" % err)
            raise err

    @ddt.data([sql03])
    @ddt.unpack
    def test_SpaceAPI_03(self, sql):
        '''关闭机构空间
        :param sql: sql语句
        :param d_index: 数据索引1
        :return:
        '''
        try:
            # 1. 调用删除空间接口
            response = self.S.Space_delete_api(sql)

            # 2. 解析数据，断言
            # 2.1状态码
            self.log.info('1.判断返回状态码：{0} = {1}'.format(200, response[0]))
            assert 200 == response[0], '返回状态不正确：{0}'.format(response[0])
            self.log.info('status_code：OK')

            # 2.2返回数据
            response = json.loads(response[1])
            self.log.info('2.判断success：{0} = {1}'.format('True', response['success']))
            assert True == response['success'], 'success状态不正确：{0}'.format(response['success'])
            self.log.info('success：OK')

        except Exception as err:
            self.log.error("test_SpaceAPI_02 : %s" % err)
            raise err
