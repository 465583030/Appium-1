# Author:Xiaojingyuan
import re


class Check:
    def __init__(self):
        self.correlationDict = {}

        # 用于解析返回值(response)

    def analysis_response(self, correlation, response):
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
                        # self.log.error(api_no + ' ' + api_name + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                        print('error!!!')
                        continue

                    # 4.返回结果赋值
                    value = response

                    # 5.继续处理correlation
                    a = correlation[1][1:-1].split('][')
                    print('a = ',a)
                    print('value = ',value)
                    # 6.循环遍历列表的键
                    for key in a:
                        try:
                            temp = value[int(key)]
                            print('temp = ',temp)
                        except:
                            try:
                                temp = value[key]
                                print('temp = ',temp)
                            except:
                                break
                        value = temp

                    assert correlation[0] == value,'不等于'

                    # self.correlationDict[correlation[0]] = value
        # return self.correlationDict

    def check(self, response, check):
        if check in response:
            print("OK!")
        else:
            print("NO!")

response = {"id": 19831, "success": 'true'}
correlation = 'true=[success]'

response1 = [{"success":'true'}]
correlation1 = 'true=[0][success]'

c = Check()
# a = c.analysis_response(correlation=correlation, response=response)
a = c.analysis_response(correlation=correlation1, response=response1)
