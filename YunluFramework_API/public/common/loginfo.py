# Author:Xiaojingyuan
from YunluFramework_API.public.common.log import Log
from YunluFramework_API.config.globalparam import GlobalParam


class LogInfo():
    def __init__(self):
        # 1.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')

        # 2.获取截图路径、日志路径、日志名
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名

        # 3.创建日志记录模块
        self.log = Log(self.logfile)

    def printlog(self, data, response, describle=None, url=None, method=None, header=None):
        '''
        打印日志模块
        :param data: 请求数据
        :param response: 返回值
        :param describle: 接口描述
        :param url: 接口地址
        :param method: 请求方法
        :param header: 头文件
        :return:
        '''
        self.log.info('1.接口描述')
        self.log.info('{0}\n'.format(describle))

        self.log.info('2.请求url')
        self.log.info('{0}\n'.format(url))

        self.log.info('3.请求方法')
        self.log.info('{0}\n'.format(method))

        self.log.info('4.请求headers')
        self.log.info('{0}\n'.format(header))

        self.log.info('5.body参数')
        self.log.info('{0}\n'.format(data))

        self.log.info('6.响应结果')
        self.log.info('{0}\n'.format(response[1]))
