# Author:Xiaojingyuan

# correlationDict = {}
# correlationDict['${self.token}'] = 'adsfaezdjkhf78dfhjia23bljadsf'
# correlationDict['${space_name}'] = 'api测试'

correlationDict = {
    '${self.token}': 'adsfaezdjkhf78dfhjia23bljadsf',
    '${space_name}': 'api测试',
    '${id}': '1',
    '${cookie}': 'aseuqo2i34'
}

parameter = {
    'token': '${self.token}',
    'q': '${space_name}',
    'class': None,
    'cookie': '${cookie}',
    '${cluster_id}':'123'
}

a = '/api/v1/clusters/${cluster_id}'

# 遍历parameter的键
# for k in parameter:
#     print('---------外层---------parameter_value = ', parameter[k])  # 总共3次
#     for key in correlationDict:
#         print('correlationDict_key = ', key)
#         if parameter[k] == key:
#             print()
#             print('找到了')
#
#             # 如果找到了，就要把parameter当前的value值赋值为correlationDict中key对应的value值
#             parameter[k] = correlationDict[key]
#             print('parameter[k] = ', parameter[k])
# print(parameter)

for k in parameter:
    if(a.find(k))>0:
        print(parameter[k])
        print(k)
        a = a.replace(k,parameter[k])
        print(a)

def analysis_url(api_url):
    '''
    用于解析url地址
    :param api_url : 接口路由
    :return:
    '''
    # 1.替换api_data中的关联项
    for k in parameter:
        if (api_url.find(k)) > 0:
            api_url = api_url.replace(k,parameter[k])
    return api_url

a = analysis_url(api_url='/api/v1/clusters/${cluster_id}')
print(a)