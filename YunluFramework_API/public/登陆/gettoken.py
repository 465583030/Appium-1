# Author:Xiaojingyuan
from YunluFramework_API.public.空间 import *


class GetToken:
    def __init__(self):
        self.login = Login()

    def get_token(self):
        # 1. 请求登录，获取token
        r = self.login.loginRequest(sql='select * from test1_1_login_01', d_index=0)
        token = json.loads(r[1])['authentication_token']
        return token
# print(GetToken().get_token())
