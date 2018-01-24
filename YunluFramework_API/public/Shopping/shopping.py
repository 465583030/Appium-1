# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.public.Shopping import *


# 空间
@ddt.ddt
class Shopping(Login):
    def __init__(self):
        Handle.__init__(self)

        #1. 创建读取配置信息对象
        self.shopping = GlobalParam('config', 'shopping.conf')

        # 2.接口路由
        # Space - 企业空间关闭
        self.Shopping_buyer_order_details_number = self.shopping.getURL('shopping','Shopping_buyer_order_details_number')

        # Shopping - 买家订单 - 下单
        self.Shopping_buyer_order_order = self.shopping.getURL('shopping','Shopping_buyer_order_order')

        # Shopping - 买家订单 - 列表
        Shopping_buyer_order_list = / api / v1 / order_forms

        # Shopping - 买家订单 - 取消订单
        Shopping_buyer_order_cancel = / api / v1 / order_forms /: number / cancel

        # hopping - 买家订单 - 提醒发货
        买家提醒发货
        Shopping_buyer_order_remind = / api / v1 / order_forms /: number / remind

        Shopping - 买家订单 - 收货
        Shopping_buyer_order_receipt = / api / v1 / order_forms /: number / receipt

        Shopping - 买家订单 - 物流轨迹
        Shopping_buyer_order_traces = / api / v1 / order_forms /: number / traces

        Shopping - 买家订单 - 申请退款
        Shopping_buyer_order_refund = / api / v1 / order_forms /: number / refund

        Shopping - 买家订单 - 评论
        用户对商品发表评论
        Shopping_buyer_order_comments = / api / v1 / order_forms /: number / comments

        Shopping - 会费订单 - 创建
        会费订单创建
        Shopping_member_fee_create = / api / v1 / order_forms / member_fee

        Shopping - 余额充值订单 - 创建
        余额充值订单创建
        Shopping_balance_create = / api / v1 / order_forms / balance

        Shopping - 卖家订单 - 列表
        Shopping_seller_order_list = / api / v1 / team /: team_id / order_forms

        Shopping - 卖家订单 - 发货
        Shopping_seller_order_deliver = / api / v1 / team /: team_id / order_forms /:number / deliver

        Shopping - 卖家订单 - 售后详情
        Shopping_seller_order_aftermarket_details = / api / v1 / team /: team_id / order_forms /:number / refund /: item_id

        Shopping - 卖家订单 - 回复评论
        Shopping_seller_order_reply_comments = / api / v1 / team /: team_id / order_forms /:number / comments

        Shopping - 卖家订单 - 处理退货
        Shopping_seller_order_deal_refund = / api / v1 / team /: team_id / order_forms /:number / refund

        Shopping - 卖家订单 - 待评价
        Shopping_seller_order_need_reply = / api / v1 / team /: team_id / order_forms / items / need_reply

        Shopping - 卖家订单 - 查看评论
        Shopping_seller_order_view_comments = / api / v1 / team /: team_id / order_forms /:number / comments

        Shopping - 卖家订单 - 物流轨迹
        Shopping_seller_order_traces = / api / v1 / team /: team_id / order_forms /:number / traces

        Shopping - 卖家订单 - 退款(售后)
        订单
        Shopping_seller_order_service = / api / v1 / order_forms / service

        Shopping - 收货地址 - 列表
        Shopping_receiving_address_list = / api / v1 / deliveries

        Shopping - 收货地址 - 删除
        Shopping_receiving_address_delete = / api / v1 / deliveries /: id

        Shopping - 收货地址 - 添加
        Shopping_receiving_address_add = / api / v1 / deliveries

        Shopping - 收货地址 - 编辑
        Shopping_receiving_address_edit = / api / v1 / deliveries /: id

        Shopping - 物流公司 - 列表
        Shopping_express_company_list = / api / v1 / express_companies

        Shopping - 采购项目 - 分单
        Shopping_purchase_items_groups = / api / v1 / purchase_items / groups

        Shopping - 采购项目 - 列表
        Shopping_purchase_items_list = / api / v1 / purchase_items

        Shopping - 采购项目 - 删除
        Shopping_purchase_items_delete = / api / v1 / purchase_items

        Shopping - 采购项目 - 添加
        Shopping_purchase_items_add = / api / v1 / purchase_items

        Shopping - 采购项目 - 编辑
        Shopping_purchase_items_edit = / api / v1 / purchase_items /: id

        # 3.token
        self.token = self.get_token()

        # 4. 创建请求对象
        self.R = RequestForHttp()

    # Space - 企业空间创建
    def Space_org_create_api(self, sql, d_index):
        '''创建机构空间
        :param token : token值
        :param sql: sql查询语句
        :param d_index: 数据索引
        :return:
        '''

        # 1.组装数据-[{...},{...}...]对象 列表-字典
        data = self.d.data_assembly(sql)
        data = data[d_index]

        # 2. 组装token和data
        data['token'] = self.token

        # 3. 发送请求
        response = self.R.post_function(self.Space_org_create, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 企业空间创建', url=self.Space_org_create, method='post')

        # 5.返回
        return response

    # Space - 文件夹列表
    def Space_folder_list_api(self, stranger_id=None, user_id=None, cluster_id=None):
        '''
        获取当前用户的文件夹
        :param stranger_id : 联系人ID  提供该值则获取该联系人下的文件夹
        :param user_id :     用户UUID  提供该值则获取该用户下的文件夹
        :param cluster_id :  私有空间ID 提供该值则获取该空间下的文件夹
        :return:
        '''
        # 1.组装数据
        # data = self.d.data_assembly(sql)
        # data = data[d_index]

        # 2.组装token和data
        key = 'token'
        data = {
            key: self.token,
            'stranger_id': stranger_id,
            'user_id': user_id,
            'cluster_id': cluster_id
        }

        # 3. 发送请求
        response = self.R.get_function(self.Space_folder_list, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 文件夹列表', url=self.Space_folder_list, method='get')

        # 5.返回
        return response

    # Space - 文件夹列表(联系人所有）
    def Space_folder_list_id_api(self, id, cluster_id):
        '''
        获取指定联系人向当前用户开放空间内的文件夹列表
        :param id :         联系人ID
        :param cluster_id : 空间ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'id': id,
            'cluster_id': cluster_id
        }

        # 2.替换id
        self.Space_folder_list_id = self.Space_folder_list_id.replace(":id", id)

        # 3.发送请求
        response = self.R.get_function(self.Space_folder_list_id, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 文件夹列表(联系人所有）', url=self.Space_folder_list_id, method='get')

        # 5.返回
        return response

    # Space - 文件夹创建
    def Space_folder_create_api(self, cluster_id, name):
        '''
        创建文件夹到私人空间
        :param cluster_id : 私有空间ID
        :param name :       文件夹名称
        :return:
        '''

        # 1.组装token和data
        data = {
            'token': self.token,
            'cluster_id': cluster_id,
            'name': name
        }

        # 2.发送请求
        response = self.R.post_function(self.Space_folder_create, data)

        # 3.打印日志
        self.plog.printlog(data, response, describle='Space - 文件夹创建', url='Space_folder_create', method='post')

        # 4.返回
        return response

    # Space - 文件夹删除
    def Space_folder_delete_id_api(self, id):
        '''
        删除当前用户的文件夹
        :param id : 文件夹id
        :return:
        '''

        # 1. 组装
        data = {
            'token': self.token,
            'id': id,
        }

        # 2. 替换id
        self.Space_folder_delete_id = self.Space_folder_delete_id.replace(":id", id)

        # 3.发送请求
        response = self.R.delete_function(self.Space_folder_delete_id, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 文件夹删除', url=self.Space_folder_delete_id, method='delete')

        # 5.返回
        return response

    # Space - 文件夹更新
    def Space_folder_update_id_api(self, id, cluster_id=None, name=None):
        '''
        更新文件夹
        :param id :         文件夹ID
        :param cluster_id : 私有空间ID
        :param name :       文件夹名称
        :return:
        '''

        # 1.组装
        data = {
            'token': self.token,
            # 'id': id,
            'cluster_id': cluster_id,
            'name': name
        }

        # 2.替换id
        url = self.Space_folder_update_id.replace(":id", id)

        # 3.发送请求
        response = self.R.put_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 文件夹更新', url=url, method='put')

        # 5.返回
        return response

    # Space - 文件夹浏览记录
    def Space_folder_browse_api(self, id, aid=None, page=None, per_page=None):
        '''
        文件夹浏览记录列表
        :param id :      文件夹ID
        :param aid :     消息ID 当从消息中查看时
        :param page:     页数
        :param per_page: 每页记录数
        :return:
        '''

        # 1.组装
        data = {
            'token': self.token,
            'id': id,
            'aid': aid,
            'page': page,
            'per_page': per_page
        }

        # 2.替换id
        url = self.Space_folder_browse.replace(":id", id)

        # 3.发送请求
        response = self.R.get_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 文件夹浏览记录', url=url, method='get')

        # 5.返回
        return response

    # Space - 热门空间名
    def Space_popular_name_api(self, class_id, count=None):
        '''
        获取常用空间名
        :param class_id :   空间类型
        :param count :      空间名数量 默认10个
        :return:
        '''
        # 1.组装
        data = {
            'token': self.token,
            'class_id': class_id,
            'count': count
        }

        # 2.发送请求
        response = self.R.get_function(self.Space_popular_name, data)

        # 3.打印日志
        self.plog.printlog(data, response, describle='Space - 热门空间名', url=self.Space_popular_name, method='get')

        # 4.返回
        return response

    # Space - 空间中删除联系人(删除客户)
    def Space_delete_contact_id_api(self, id, stranger_ids):
        '''
        从当前用户的空间删除联系人
        :param id :             私有空间ID
        :param stranger_ids :   联系人ID
        :return:
        '''

        # 1.组装
        data = {
            'token': self.token,
            'id': id,
            'stranger_ids[]': stranger_ids
        }

        # 2.替换id
        url = self.Space_delete_contact_id.replace(":id", id)

        # 3.发送请求
        response = self.R.delete_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 空间中删除联系人(删除客户)', url=url, method='delete')

        # 5.返回
        return response

    # Space - 空间中添加联系人(新增客户)
    def Space_add_contac_id_api(self, id, stranger_ids):
        '''
        从当前用户的空间删除联系人
        :param id :             私有空间ID
        :param stranger_ids :   联系人ID
        :return:
        '''

        # 1.组装
        data = {
            'token': self.token,
            'id': id,
            'stranger_ids[]': stranger_ids
        }

        # 2.替换id
        url = self.Space_add_contac_id.replace(":id", id)

        # 3.发送请求
        response = self.R.post_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 空间中添加联系人(新增客户)', url=url, method='post')

        # 5.返回
        return response

    # Space - 空间公开设置
    def Space_switch_setting_api(self, id, disclosure):
        '''
        对个人空间设置公开与否
        :param clusters_id :         空间ID
        :param clusters_disclosure : 开关-允许值: ['on', 'off']
        :return:
        '''

        # 1.组装
        data = {
            "token": self.token,
            "clusters": [
                {
                    "id": id,
                    "disclosure": disclosure
                }
            ]
        }

        # 2.将字典格式转化成json
        data = json.dumps(data)

        # 3.定制请求头
        headers = {
            "Content-Type": "application/json"
        }

        # 4.发送请求
        response = self.R.post_function(self.Space_switch_setting, data, headers=headers)

        # 5.打印日志
        self.plog.printlog(data, response, describle='Space - 空间公开设置', url=self.Space_switch_setting, method='post')

        # 6.返回
        return response

    # Space - 空间列表
    def Space_list_api(self, q=None, class_type=None):
        # 1.组装token
        data = {
            'token': self.token,
            'q': q,
            'class': class_type
        }

        # 2. 发送请求
        response = self.R.get_function(self.Space_list, data)

        # 3.打印日志
        self.plog.printlog(data, response, describle='Space - 空间列表', url=self.Space_list, method='get')

        # 4.返回
        return response

    # Space - 空间创建（私人空间）
    def Space_private_create_api(self, name, class_id):
        '''
        当前用户创建私人空间
        :param name :       空间名称
        :param class_id :   空间类型
        :return:
        '''

        # 1.组装token
        data = {
            'token': self.token,
            'name': name,
            'class_id': class_id
        }

        # 2. 发送请求
        response = self.R.post_function(self.Space_private_create, data)

        # 3.打印日志
        self.plog.printlog(data, response, describle='Space - 私人空间创建', url=self.Space_private_create, method='post')

        # 4.返回
        return response

    # Space - 空间删除（私人空间）
    def Space_private_delete_id_api(self, id):
        '''
        删除当前用户的私人空间
        :param id : 空间id
        :return:
        '''

        # 1.组装数据
        data = {
            'token': self.token,
            'id': id
        }

        # 2.替换id
        url = self.Space_private_delete_id.replace(':id', id)

        # 3. 发送请求
        response = self.R.delete_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 私人空间删除', url=url, method='delete')

        # 5.返回
        return response

    # Space - 空间更新（私人空间）
    def Space_update_id_api(self, id, name=None, class_id=None):
        '''
        更新私人空间
        :param id :         空间ID
        :param name :       空间名称
        :param class_id:    空间类型ID
        :return:
        '''

        # 1.组装数据
        data = {
            'token': self.token,
            'id': id,
            'name': name,
            'class_id': class_id
        }

        # 2.替换id
        url = self.Space_update_id.replace(':id', id)

        # 3.发送请求
        response = self.R.put_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 空间更新', url=url, method='put')

        # 5.返回
        return response

    # Space - 空间概况（私人空间）
    def Space_overview_id_api(self, id):
        '''
        空间概况
        :param id : 空间ID
        :return:
        '''

        # 1.组装数据
        data = {
            'token': self.token,
            'id': id
        }

        # 2.替换id
        url = self.Space_overview_id.replace(':id', id)

        # 3.发送请求
        response = self.R.get_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 空间概况', url=url, method='get')

        # 5.返回
        return response

    # Space - 私人空间类型列表
    def Space_private_type_list_api(self, parent_id=None):
        # 1.组装token
        data = {
            'token': self.token,
            'parent_id': parent_id
        }

        # 2. 发送请求
        response = self.R.get_function(self.Space_type_list, data)

        # 3.打印日志
        self.plog.printlog(data, response, describle='Space - 私人空间类型列表', url=self.Space_type_list, method='get')

        # 4.返回数据
        return response

    # Space - 空间联系人列表(非当前用户)
    def Space_contact_list_id_api(self, id, page=None, per_page=None):
        '''
        :param id :         空间ID
        :param page :       页数
        :param per_page :   每页记录数
        :return:
        '''

        # 1.组装数据
        data = {
            'token': self.token,
            'id': id,
            'page': page,
            'per_page': per_page
        }

        # 2.替换id
        url = self.Space_contact_list_id.replace(":id", id)

        # 3.发送请求
        response = self.R.get_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 空间联系人列表(非当前用户)', url=url, method='get')

        # 5.返回
        return response

    # Space - 企业空间关闭
    def Space_delete_api(self, sql):
        '''关闭空间
        :param sql: sql查询语句
        :param d_index: 数据索引
        :return:
        '''

        # 1.查询organzation_id
        organization_id = self.d.select(sql)[0][0]

        # 2.组装url
        part_url = '/%s/organization' % organization_id
        url = self.url_closespace + part_url

        # 3. 组装token和data
        # 创建data字典
        key = 'token'
        data = {key: self.token}

        # 4. 发送请求
        response = self.R.delete_function(url, data)
        self.plog.printlog(data, response, describle='Space - 企业空间关闭', url=self.url_closespace, method='delete')

        # 5.返回
        return response


# 调试

# Space - 文件夹列表
# sp.Space_folder_list_api(cluster_id='4073')

# Space - 文件夹列表(联系人所有）
# sp.Space_folder_list_id_api(id='183262',cluster_id='3464')

# Space - 文件夹创建
# sp.Space_folder_create_api(cluster_id='4073',name='api测试')

# Space - 文件夹删除
# sp.Space_folder_delete_id_api(id='19710')

# Space - 文件夹更新
# sp.Space_folder_update_id_api(id='8299',cluster_id='19768',name='api测试1')

# Space - 文件夹浏览记录
# sp.Space_folder_browse_api(id='19711')

# Space - 热门空间名
# sp.Space_popular_name_api(class_id='66')

# Space - 空间中删除联系人(删除客户)
# sp.Space_delete_contact_id_api(id='4073',stranger_ids='183262')

# Space - 空间中添加联系人(新增客户)
# sp.Space_add_contac_id_api(id='4073',stranger_ids='183262')

# Space - 空间公开设置
# sp.Space_switch_setting_api("4073", "off")

# Space - 私人空间创建
# sp.Space_private_create_api(name='api测试', class_id='67')

# Space - 私人空间删除
# sp.Space_private_delete_id_api(id='8248')

# Space - 空间更新
# sp.Space_update_id_api(id='8248',name='空间更新api',class_id='68')

# Space - 空间概况
# sp.Space_overview_id_api(id='8248')

# Space - 空间联系人列表(非当前用户) ———— 弃用
# sp.Space_contact_list_id_api(id='8248')

# Space - 私人空间类型列表
# sp.Space_private_type_list_api()

# sp.Space_list_api(q='api测试')
