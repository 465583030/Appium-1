# Author:Xiaojingyuan
import requests
import json
from YunluFramework_API.public.common.log import Log
from YunluFramework_API.config.globalparam import GlobalParam


# 用于处理请求的Get和Post方法
class RequestForHttp:
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 3.创建日志记录模块
        self.log = Log(self.logfile)

    def get_function(self, url, r_data):
        '''
        get请求
        :param url: 接口地址
        :param data: 数据
        :return:
        '''
        try:
            # 1.发送请求
            r = requests.get(url, params=r_data)
            # self.log.info('POST请求：\n请求地址：{0} \n请求参数：{1}'.format(url, r_data))
            # 2.打印请求状态码
            status = r.status_code
            # self.log.info('请求状态码为：{0}'.format(status))
            # 3.打印返回结果
            response = r.text
            # 4.解码json数据,将json转为字典
            dict_r = json.loads(response)
            # 5.格式化输出json
            # ensure_ascii=False 中文不转码
            json_r = json.dumps(dict_r, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
            return [status, json_r]
        except Exception as err:
            self.log.error("GET请求错误 : %s" % err)
            raise err

    def post_function(self, url, r_data):
        '''
        post请求
        :param url: 接口地址
        :param r_data: 数据
        :return:
        '''
        try:
            # 1.发送请求
            r = requests.post(url, data=r_data)
            # self.log.info('POST请求：\n请求地址：{0} \n请求参数：{1}'.format(url, r_data))
            # 2.打印请求状态码
            status = r.status_code
            # self.log.info('请求状态码为：{0}'.format(status))
            # 3.打印返回结果
            response = r.text
            # 4.解码json数据,将json转为字典
            dict_r = json.loads(response)
            # 5.格式化输出json
            # ensure_ascii=False 中文不转码
            json_r = json.dumps(dict_r, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
            return [status, json_r]
        except Exception as err:
            self.log.error("POST请求错误 : %s" % err)
            raise err

    def delete_function(self, url, r_data):
        '''
        post请求
        :param url: 接口地址
        :param r_data: 数据
        :return:
        '''
        try:
            # 1.发送请求
            r = requests.delete(url, data=r_data)
            # self.log.info('POST请求：\n请求地址：{0} \n请求参数：{1}'.format(url, r_data))
            # 2.打印请求状态码
            status = r.status_code
            # self.log.info('请求状态码为：{0}'.format(status))
            # 3.打印返回结果
            response = r.text
            # 4.解码json数据,将json转为字典
            dict_r = json.loads(response)
            # 5.格式化输出json
            # ensure_ascii=False 中文不转码
            json_r = json.dumps(dict_r, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
            return [status, json_r]
        except Exception as err:
            self.log.error("DELETE请求错误 : %s" % err)
            raise err
