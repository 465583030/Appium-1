# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.testcase.SpaceAPI import *
from YunluFramework_API.testcase.SpaceAPI.TestSapceData import SpaceAPI_Dada
from YunluFramework_API.public.common.test_excel import Excel
from YunluFramework_API.api_test.api_request import API_REQUEST
import json


@ddt.ddt
class SpaceAPI_Private(unittest.TestCase, SpaceAPI_Dada):
    # 全局数据: 获取excel中行数据
    request = API_REQUEST(sheet_name='test2')
    excel1 = Excel(xls='data_api.xls', sheet_name='test2')
    data = excel1.get_row_data(sheet_name='test2')

    # 1.类开始
    @classmethod
    def setUpClass(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 3.创建日志记录模块
        self.log = Log(self.logfile)

        # 4.打印日志
        self.log.info('****************************************SpaceAPI_Private：开始****************************************')

        # 5.创建登录对象
        self.S = Space()

    # 2.类结束
    @classmethod
    def tearDownClass(self):
        # 1.打印日志
        self.log.info('****************************************SpaceAPI_Private：结束****************************************\n')

    # 3.测试方法开始
    def setUp(self):
        self.log.info('------------------------------------用例开始------------------------------------')

    # 4.测试方法结束
    def tearDown(self):
        self.log.info('------------------------------------用例结束------------------------------------\n')

    # 4.测试用例
    @ddt.data(*data)
    def test_api(self, list):
        '''
        :param list: 参数化列表
        :return:
        '''
        # 1.控制器
        api_no = list[0]  # 接口编号
        api_name = list[1]  # 接口名称
        api_describe = list[2]  # 接口描述
        api_url = list[3]  # 接口路由
        api_function = list[4]  # 接口方法
        api_headers = list[5]  # 接口头部
        api_data = list[6]  # 接口数据
        api_check = list[7]  # 接口检查
        api_hope = list[8]  # 接口预期
        api_active = list[10]  # 接口执行
        api_status = list[11]  # 预期状态
        api_correlation = list[12]  # 接口关联

        # 2.用例执行
        response = ''
        status_code = ''

        if api_active == 'YES':
            try:
                # 发送请求
                response = self.request.api_requests(api_no=api_no, api_name=api_name, api_describe=api_describe,
                                                     api_url=api_url, api_function=api_function, api_headers=api_headers,
                                                     api_data=api_data, api_check=api_check, api_hope=api_hope,
                                                     api_status=api_status, api_correlation=api_correlation)
                # 解析状态码
                status_code = response[0]

                # 解析返回值
                response = response[1]
            except Exception as e:
                self.log.error('Exception Information : {0}'.format(e))

            # 断言1:返回值是否为空
            try:
                assert response != ''
            except Exception as e:
                self.log.error('返回值为空！\n')
                assert False, '返回值为空！'

            # 断言2:status状态码是否正确
            try:
                assert status_code == api_status
            except Exception as e:
                self.log.error('返回状态码错误！实际返回状态码为:{0}\n'.format(status_code))
                assert False, '返回状态码错误！实际返回状态码为:{0}'.format(status_code)

            # 断言3:检查点数据校验
            # 如果api_check不为空：
            try:
                if api_check != '':
                    assert False != self.request.analysis_check(api_no=api_no, api_name=api_name, api_check=api_check, response=response)
                else:
                    pass
            except Exception as e:
                self.log.error('检查点:{0} | 结果错误,错误信息:{1}'.format(api_check, e))
                assert False, '检查点:{0} | 结果错误，错误信息:{1}'.format(api_check, e)

            # 断言4:返回值是否符合预期
            # 如果api_hope不为空:
            if api_hope != '':
                # 1> 先将api_hope通过json解析成对应的格式
                api_hope = json.loads(api_hope)

                # 2> 断言
                try:
                    assert api_hope == response
                except Exception as e:
                    self.log.error('实际结果与预期结果不符！')
                    assert False, '实际结果与预期结果不符！'
            else:
                pass

        # 3.用例不执行
        elif api_active == 'NO':
            self.log.info(list)
            self.log.info('未执行测试用例编号 : {0} | 名称 : {1}'.format(api_no, api_name))
            pass
