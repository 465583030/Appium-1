# Author:Xiaojingyuan
import re
# 配置关联字典
correlationDict = {}

# 关联原始数据
correlation = '${session_id}=[session];${token_id}=[token]'
# correlation_13 = '${cluster_id}=[0][cluster_id];${name}=[0][name]'
correlation = '${cluster_id}=[token]'


# 处理关联数据(存到列表中)
correlation = correlation.replace('\n', '').replace('\r', '').split(';')
# correlation = correlation_13.replace('\n', '').replace('\r', '').split(';')

# 返回值
resp = {'token': 'token_12345678', 'session': 'session_id_123456'}
# resp1 = [{'token': 'token_12345678', 'session': 'session_id_123456'}]

# resp = [
#     {
#         "aliaz": 'null',
#         "class_id": 67,
#         "cluster_id": 8371,
#         "company": 'null',
#         "disclosure": "off",
#         "gallery_count": 0,
#         "locked": 'false',
#         "logo_url": 'null',
#         "name": "api测试",
#         "organization_id": 'null',
#         "owner_class": "private",
#         "service_id": 'null',
#         "vocation": 'null'
#     }
# ]



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
        value = resp
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
print()
print('correlationDict = ',correlationDict)
