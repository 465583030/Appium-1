# Author:Xiaojingyuan
import re

correlationDict = {}
correlation = '${cluster_id}=[id]'
response = {
    'id': 1234
}


def analysis_response(correlation, response):
    '''
    用于解析返回值中的数据，将这些数据存入字典中以供使用
    :param response : 接口返回值
    :return:
    '''
    # 如果关联数据不为空
    if correlation != '':
        # 1.处理关联数据(存到列表中)
        _correlation = correlation.replace('\n', '').replace('\r', '').split(';')

        # 2.分解关联数据
        for j in range(len(_correlation)):
            _correlation = _correlation[j].split('=')

            # 3.判断处理后的关联列表长度为2时
            if len(_correlation) == 2:
                if _correlation[1] == '' or not re.search(r'^\[', _correlation[1]) or not re.search(r'\]$', _correlation[1]):
                    # log.error(api_no + ' ' + api_name + ' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                    continue

                # 4.返回结果赋值
                res = response

                # 5.继续处理_correlation
                _correlation = _correlation[1][1:-1].split('][')

                # 6.循环遍历列表的键
                for key in _correlation:
                    try:
                        temp = res[int(key)]
                    except:
                        try:
                            temp = res[key]
                        except:
                            break
                    res = temp
                correlationDict[_correlation[0]] = res
    return correlationDict






def analysis_response1(correlation, response):
    correlation = correlation.replace('\n', '').replace('\r', '').split(';')
    for j in range(len(correlation)):
        param = correlation[j].split('=')
        print('param值 = ')
        # param的值
        # ['${session}', '[session]']
        # ['${token}', '[token]']

        if len(param) == 2:
            if param[1] == '' or not re.search(r'^\[', param[1]) or not re.search(r'\]$', param[1]):
                print(' 关联参数设置有误，请检查[Correlation]字段参数格式是否正确！！！')
                continue
            value = response
            print('value = ',value)                     #-------------value(返回值)-------------



            a = param[1][1:-1].split('][')
            print('a = ',a)                              #------------- a -------------
            # 打印a的值
            # a = ['session']
            # a = ['token']

            for key in a:
                print('key = ',key)                      #-------------key-------------
                print()
                try:
                    temp = value[int(key)]
                except:
                    try:
                        temp = value[key]
                        print('temp = ',temp)
                    except:
                        break
                value = temp
            correlationDict[param[0]] = value
    return correlationDict

a = analysis_response1(correlation,response)
print(a)