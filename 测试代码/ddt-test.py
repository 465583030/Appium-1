# Author:Xiaojingyuan
import unittest
import ddt


testData1=[{"username":"selenium群"},
          {"username":"python群"},
          {"username":"appium群"}]

a1 = [["{'token': 'self.token', 'parent_id': None}", "{'token': 'self.token'}"],
      ["{'token1': 'self.token', 'parent_id1': None}", "{'token1': 'self.token'}"]]

testData2 = ['appium测试空间', 'appium测试空间', '北京', '东城', 1]
testData3 = [{'token': 'self.token','q': 'api测试', 'class': None},
             {'token': 'self.token','q': 'api测试', 'class': None}]

@ddt.ddt
class space_CreateO(unittest.TestCase):

    @ddt.data(a1)
    @ddt.unpack
    def test01(self,A,B):
        print(A)
        print(B)