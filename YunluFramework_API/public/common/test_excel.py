from YunluFramework_API.public.common.datainfo import DataInfo


class Excel:
    def __init__(self, xls, sheet_name):
        # .创建excel操作对象
        self.d = DataInfo(path=xls)

        # 获取表单行数
        self.len = self.d.get_rows(sheet_name=sheet_name)

        # 初始化表单名
        self.sheet_name = sheet_name

    def excel_data(self, description):
        '''
        统计接口测试用例描述信息次数
        :param description:
        :return:
        '''
        api_description_flag = 0
        row_no = 0

        for i in range(2, self.len + 1):
            # 1.接口描述
            api_description = str(self.d.cell(sheet_name=self.sheet_name, rowno=i, colno=2))

            # 2.记录接口描述次数
            if api_description == description:
                api_description_flag += 1

                # 当描述第一次被找到的时候，记录当前行数
                if api_description_flag == 1:
                    row_no = i
                else:
                    pass

        return [api_description_flag, row_no]

    def get_data(self, description):
        '''
        获取测试数据
        :param description ：描述信息
        :return:
        '''
        # 1.申明列表
        list = []

        # 2.存描述次数
        description_row_no = self.excel_data(description)
        flag = description_row_no[0]
        row_no = description_row_no[1]

        if flag == 1:
            # list.append(eval(self.d.cell(sheet_name=self.sheet_name, rowno=row_no, colno=7)))
            list.append((self.d.cell(sheet_name=self.sheet_name, rowno=row_no, colno=7)))
            return list


        elif flag > 1:

            for i in range(row_no, row_no + flag):
                a = self.d.cell(sheet_name=self.sheet_name, rowno=i, colno=7)  # a:字符串
                # list.append(eval(a)) #将a转换成字典
                list.append((a))  # 将a转换成字典
            return list

        else:
            list.append(None)
            return list

    def get_result(self, description):
        '''
        获取测试数据
        :param description ：描述信息
        :return:
        '''
        # 1.申明列表
        list = []

        # 2.存描述次数
        description_row_no = self.excel_data(description)
        flag = description_row_no[0]
        row_no = description_row_no[1]

        if flag == 1:
            list.append((self.d.cell(sheet_name=self.sheet_name, rowno=row_no, colno=9)))
            return list


        elif flag > 1:

            for i in range(row_no, row_no + flag):
                a = self.d.cell(sheet_name=self.sheet_name, rowno=i, colno=9)  # a:字符串
                # list.append(eval(a)) #将a转换成字典
                list.append((a))
            return list

        else:
            list.append(None)
            return list

    def write_cell(self, description, sheet_name, result):
        '''
        将结果写入excel表中
        :param result : 测试结果
        :return:
        '''
        description_row_no = self.excel_data(description)
        flag = description_row_no[0]  # 循环写入次数
        row_no1 = description_row_no[1]  # 从第几行开始写

        #1.循环写入
        for i in range(1,flag+1):
            self.d.write_data(sheet_name=sheet_name, rowno=row_no1, colno=10, result=result)

ex = Excel(xls='data_api.xls', sheet_name='SPACE')
# a = ex.get_data(description='Space - 空间列表')
# print(a)

# a = ex.get_result(description='Space - 空间类型列表（私人空间）')
# print(a)

result = 'asdfasdfasdf'
ex.write_cell(description='Space - 空间类型列表（私人空间）',sheet_name='SPACE',result=result)
