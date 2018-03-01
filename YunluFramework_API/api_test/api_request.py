# Author:Xiaojingyuan
from YunluFramework_API.api_test import *
from YunluFramework_API.public.common.test_excel import Excel
import re
import json


class API_REQUEST(Login):
    def __init__(self, sheet_name):
        Handle.__init__(self)
        # 1.sheet_name
        self.sheet_name = sheet_name

        # 2.token
        self.token = self.get_token()

        # 3. 创建请求对象
        self.R = RequestForHttp()

        # 4.获取excel中行数据
        self.excel = Excel(xls='data_api.xls', sheet_name=self.sheet_name)
        self.data = self.excel.get_row_data(sheet_name=self.sheet_name)

        # 5.关联字典
        # 关联字典
        self.correlationDict = {}
        self.checkDict = {}

        # 其中内置了四个参数，分别是：
        # ${token}（token令牌值）
        # ${randomTel}（随机手机号码）
        # ${timestamp}（当前时间戳）
        # ${session}（session#id，默认为None）
        # ${hashPassword}（hash加密密码，明文123456）

        self.correlationDict['${self.token}'] = self.token
        self.correlationDict['${space_name}'] = 'api测试'

    def print_log(self, api_no, api_name, api_describe, api_url, api_function, api_headers,
                  api_data, api_check, api_status, api_hope, response):
        '''
        打印日志模块
        :param api_no       : 接口编号
        :param api_name     : 接口名称
        :param api_describe : 接口描述
        :param api_url      : 接口地址
        :param api_function : 接口方法
        :param api_headers  : 接口头部
        :param api_data     : 接口数据
        :param api_check    : 接口检查
        :param api_hope     : 接口预期
        :param response     : 接口返回
        :return:
        '''
        self.log.info('1. 接口编号 : {0}'.format(api_no))
        self.log.info('2. 接口名称 : {0}'.format(api_name))
        self.log.info('3. 接口描述 : {0}'.format(api_describe))
        self.log.info('4. 接口路由 : {0}'.format(api_url))
        self.log.info('5. 接口方式 : {0}'.format(api_function))
        self.log.info('6. 接口头部 : {0}'.format(api_headers))
        self.log.info('7. 接口数据 : {0}'.format(api_data))
        self.log.info('8. 接口检查 : {0}'.format(api_check))
        self.log.info('9. 预期状态 ：{0}'.format(api_status))
        self.log.info('10.接口预期 : {0}'.format(api_hope))
        self.log.info('11.接口返回 : {0}'.format(response[1]))

    def api_method(self, method, api_url, data, api_headers):
        '''
        请求方式选择器
        :param method       : 请求方式
        :param api_url      : 接口路由
        :param data         : 请求数据
        :param api_headers  : 请求头
        :return:
        '''
        if method == 'GET':
            response = self.R.get_function(api_url, data)
            return response

        elif method == 'POST':
            response = self.R.post_function(api_url, data, api_headers)
            return response

        elif method == 'DELETE':
            response = self.R.delete_function(api_url, data)
            return response

        elif method == 'PUT':
            response = self.R.put_function(api_url, data)
            return response

        else:
            pass

    ''' 
        通用的接口请求方法,返回接口的response值
    '''

    def api_requests(self, api_no, api_name, api_describe, api_url, api_function, api_headers,
                     api_data, api_check, api_hope, api_status, api_correlation):
        '''
        公用请求方法
        :param api_no       : 接口编号
        :param api_name     : 接口名称
        :param api_describe : 接口描述
        :param api_url      : 接口地址
        :param api_function : 接口方法
        :param api_headers  : 接口头部
        :param api_data     : 接口数据
        :param api_check    : 接口检查
        :param api_hope     : 接口预期
        :return             : 接口返回 response[0] - 状态码 | response[1] - 返回值
        '''

        # 1.组装token
        try:
            # 1.1解析测试数据
            data = self.analysis_data(api_data)

            # 1.2 解析url
            api_url = self.analysis_url(api_url)

        except Exception as e:
            # 1.1 将请求数据转换成字典
            data = api_data
            data = eval(data)

            # 1.2 解析url
            api_url = self.analysis_url(api_url)
            self.log.error(e)

        # 2. 发送请求
        response = self.api_method(method=api_function, api_url=api_url, data=data, api_headers=api_headers)

        # 3. 打印日志
        self.print_log(api_no, api_name, api_describe, api_url, api_function, api_headers,
                       data, api_check, api_hope, api_status, response)

        # 4.解析返回值
        status_code = response[0]  # 状态码
        response1 = json.loads(response[1])  # 解析返回值
        self.analysis_response(api_no, api_name, api_correlation, response1)

        return status_code, response1

    '''
        用于解析返回值中的数据和请求数据中的关联项
    '''

    # 用于解析请求地址(api_data)
    def analysis_url(self, api_url):
        '''
        用于解析url地址
        :param api_url : 接口路由
        :return:
        '''
        # 1.替换api_data中的关联项
        for k in self.correlationDict:
            if (api_url.find(k)) > 0:
                # 此处将id team_id等参数获取到后转换成str类型
                api_url = api_url.replace(k, str(self.correlationDict[k]))
        return api_url

    # 用于解析请求数据(api_data)
    def analysis_data(self, api_data):
        '''
        用于解析关联数据，将需要关联的字段存到关联字典中
        :param api_data : 接口请求数据
        :return:
        '''
        # 1.请求数据：字符串转字典
        dic_api_data = eval(api_data)

        # 2.循环遍历测试数据
        for k in dict(dic_api_data):
            for key in self.correlationDict:
                if dic_api_data[k] == key:
                    dic_api_data[k] = self.correlationDict[key]
        return dic_api_data

    # 用于解析返回值(response)
    def analysis_response(self, api_no, api_name, correlation, response):
        '''
        用于解析返回值中的数据，将这些数据存入关联字典中以供使用
        :param response : 接口返回值
        :return:
        '''
        # 如果关联数据不为空
        if correlation != '':
            # 1.处理关联数据(存到列表中)
            correlation = correlation.replace('\n', '').replace('\r', '').split(';')

            # 2.分解关联数据
            for j in range(len(correlation)):
                correlation = correlation[j].split('=')

                # 3.判断处理后的关联列表长度为2时
                if len(correlation) == 2:
                    if correlation[1] == '' or not re.search(r'^\[', correlation[1]) or not re.search(r'\]$', correlation[1]):
                        self.log.error(api_no + ' ' + api_name + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                        continue

                    # 4.返回结果赋值
                    value = response

                    # 5.继续处理correlation
                    a = correlation[1][1:-1].split('][')

                    # 6.循环遍历列表的键
                    for key in a:
                        try:
                            temp = value[int(key)]
                        except:
                            try:
                                temp = value[key]
                            except:
                                break
                        value = temp
                    self.correlationDict[correlation[0]] = value
        return self.correlationDict

    # 用于解析检查点
    def analysis_check(self, api_no, api_name, api_check, response):
        '''
        用于检查点的校验
        :param response : 接口返回值
        :return:
        '''
        # 标志符
        flag = ''

        # 如果检查数据不为空
        if api_check != '':
            # 1.处理关联数据(存到列表中)
            api_check = api_check.replace('\n', '').replace('\r', '').split(';')
            # print('api_check = ',api_check)

            # 2.分解关联数据
            for j in range(len(api_check)):

                # 判断是否为'='关系
                if '=' in api_check[j]:

                    # 如果 '#len#' 存在
                    if '#len#' in api_check[j]:
                        # print('去除指定的 #len# 字符串 ：', api_check[j].strip('#len#'))
                        param = api_check[j].replace('#len#', '').split('=')
                        flag = '#len#'

                    # 如果 '#len#'不存在
                    elif '#len#' not in api_check[j]:
                        param = api_check[j].split('=')
                        # print('没进入 #len# 的param = ', param)
                        flag = ''

                # 判断是否为'<>'关系
                elif '<>' in api_check[j]:
                    param = api_check[j].split('<>')
                    flag = '<>'

                # 3.判断处理后的关联列表长度为2时
                if len(param) == 2:
                    if param[1] == '' or not re.search(r'^\[', param[1]) or not re.search(r'\]$', param[1]):
                        self.log.error(api_no + ' ' + api_name + ' 关联参数设置有误，请检查[Check]字段参数格式是否正确！！！')
                        continue

                    # 4.返回结果赋值
                    value = response

                    # 5.继续处理api_check
                    a = param[1][1:-1].split('][')
                    # print('a = ',a)

                    # 6.循环遍历列表的键
                    for key in a:
                        try:
                            temp = value[int(key)]
                        except:
                            try:
                                temp = value[key]
                            except:
                                break
                        value = temp
                        # print('value = ',value)

                try:
                    # 检查点数据校验
                    # '='关系断言
                    if flag == '=':
                        # print('等于')

                        # 先将value值中的True或False的类型转换成str类型，再与param[0]断言
                        if param[0] in 'True' or 'False':
                            value = str(value)
                            assert param[0] == value

                        # 如果返回数据为int型，比较时将excel中的数据先转换成整型数据
                        elif type(value) == int:
                            # print('进入elif')
                            assert int(param[0]) == value

                        # 无需转换时，直接比较检查点
                        else:
                            # print('进入else')
                            assert param[0] == value

                    # '<>'关系断言
                    if flag == '<>':
                        # 先将value值中的True或False的类型转换成str类型，再与param[0]断言
                        if param[0] in 'True' or 'False':
                            value = str(value)
                            assert param[0] != value

                        # 如果返回数据为int型，比较时将excel中的数据先转换成整型数据
                        elif type(value) == int:
                            # print('进入elif')
                            assert int(param[0]) != value

                        # 无需转换时，直接比较检查点
                        else:
                            # print('进入else')
                            assert param[0] != value

                    # '#len#'关系断言
                    if flag == '#len#':
                        # print('进入#len#')
                        assert len(value) == int(param[0])

                except Exception as e:
                    # print('进入exception')
                    return False

# request = API_REQUEST(sheet_name='test2')
# excel = Excel(xls='data_api.xls', sheet_name='test2')
# data = excel.get_row_data(sheet_name='test2')
#
# for i in range(0, len(data)):
#     api_no = data[i][0]  # 接口编号
#     api_name = data[i][1]  # 接口名称
#     api_describe = data[i][2]  # 接口描述r
#     api_url = data[i][3]  # 接口路由
#     api_function = data[i][4]  # 接口方法
#     api_headers = data[i][5]  # 接口头部
#     api_data = data[i][6]  # 接口数据
#     api_check = data[i][7]  # 接口检查
#     api_hope = data[i][8]  # 接口预期
#     api_active = data[i][10]  # 接口执行
#     api_status = (data[i][11])  # 预期状态
#     api_correlation = data[i][12]  # 接口关联
#
#     if api_active == 'YES':
#         # 发送请求
#         a = request.api_requests(api_no, api_name, api_describe, api_url, api_function, api_headers,
#                              api_data, api_check, api_hope, api_status, api_correlation)
#     else:
#         pass
