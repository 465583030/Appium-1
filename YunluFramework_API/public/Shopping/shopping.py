# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.public.Shopping import *


# 空间
@ddt.ddt
class Shopping(Login):
    def __init__(self):
        Handle.__init__(self)

        # 1. 创建读取配置信息对象
        self.shopping = GlobalParam('config', 'shopping.conf')

        # 2.接口路由
        # Space - 企业空间关闭
        self.Shopping_buyer_order_details_number = self.shopping.getURL('shopping', 'Shopping_buyer_order_details_number')

        # Shopping - 买家订单 - 下单
        self.Shopping_buyer_order_order = self.shopping.getURL('shopping', 'Shopping_buyer_order_order')

        # Shopping - 买家订单 - 列表
        self.Shopping_buyer_order_list = self.shopping.getURL('shopping', 'Shopping_buyer_order_list')

        # Shopping - 买家订单 - 取消订单
        self.Shopping_buyer_order_cancel = self.shopping.getURL('shopping', 'Shopping_buyer_order_cancel')

        # hopping - 买家订单 - 提醒发货
        self.Shopping_buyer_order_remind = self.shopping.getURL('shopping', 'Shopping_buyer_order_cancel')

        # Shopping - 买家订单 - 收货
        self.Shopping_buyer_order_receipt = self.shopping.getURL('shopping', 'Shopping_buyer_order_receipt')

        # Shopping - 买家订单 - 物流轨迹
        self.Shopping_buyer_order_traces = self.shopping.getURL('shopping', 'Shopping_buyer_order_traces')

        # Shopping - 买家订单 - 申请退款
        self.Shopping_buyer_order_refund = self.shopping.getURL('shopping', 'Shopping_buyer_order_refund')

        # Shopping - 买家订单 - 评论
        self.Shopping_buyer_order_comments = self.shopping.getURL('shopping', 'Shopping_buyer_order_comments')

        # Shopping - 会费订单 - 创建
        self.Shopping_member_fee_create = self.shopping.getURL('shopping', 'Shopping_member_fee_create')

        # Shopping - 余额充值订单 - 创建
        self.Shopping_balance_create = self.shopping.getURL('shopping', 'Shopping_balance_create')

        # Shopping - 卖家订单 - 列表
        self.Shopping_seller_order_list = self.shopping.getURL('shopping', 'Shopping_seller_order_list')

        # hopping - 卖家订单 - 发货
        self.Shopping_seller_order_deliver = self.shopping.getURL('shopping', 'Shopping_seller_order_deliver')

        # Shopping - 卖家订单 - 售后详情
        self.Shopping_seller_order_aftermarket_details = self.shopping.getURL('shopping', 'Shopping_seller_order_aftermarket_details')

        # Shopping - 卖家订单 - 回复评论
        self.Shopping_seller_order_reply_comments = self.shopping.getURL('shopping', 'Shopping_seller_order_reply_comments')

        # Shopping - 卖家订单 - 处理退货
        self.Shopping_seller_order_deal_refund = self.shopping.getURL('shopping', 'Shopping_seller_order_deal_refund')

        # Shopping - 卖家订单 - 待评价
        self.Shopping_seller_order_need_reply = self.shopping.getURL('shopping', 'Shopping_seller_order_need_reply')

        # Shopping - 卖家订单 - 查看评论
        self.Shopping_seller_order_view_comments = self.shopping.getURL('shopping', 'Shopping_seller_order_view_comments')

        # Shopping - 卖家订单 - 物流轨迹
        self.Shopping_seller_order_traces = self.shopping.getURL('shopping', 'Shopping_seller_order_traces')

        # Shopping - 卖家订单 - 退款(售后)
        self.Shopping_seller_order_service = self.shopping.getURL('shopping', 'Shopping_seller_order_service')

        # Shopping - 收货地址 - 列表
        self.Shopping_receiving_address_list = self.shopping.getURL('shopping', 'Shopping_receiving_address_list')

        # Shopping - 收货地址 - 删除
        self.Shopping_receiving_address_delete = self.shopping.getURL('shopping', 'Shopping_receiving_address_delete')

        # Shopping - 收货地址 - 添加
        self.Shopping_receiving_address_add = self.shopping.getURL('shopping', 'Shopping_receiving_address_add')

        # Shopping - 收货地址 - 编辑
        self.Shopping_receiving_address_edit = self.shopping.getURL('shopping', 'Shopping_receiving_address_edit')

        # Shopping - 物流公司 - 列表
        self.Shopping_express_company_list = self.shopping.getURL('shopping', 'Shopping_express_company_list')

        # Shopping - 采购项目 - 分单
        self.Shopping_purchase_items_groups = self.shopping.getURL('shopping', 'Shopping_purchase_items_groups')

        # Shopping - 采购项目 - 列表
        self.Shopping_purchase_items_list = self.shopping.getURL('shopping', 'Shopping_purchase_items_list')

        # Shopping - 采购项目 - 删除
        self.Shopping_purchase_items_delete = self.shopping.getURL('shopping', 'Shopping_purchase_items_delete')

        # Shopping - 采购项目 - 添加
        self.Shopping_purchase_items_add = self.shopping.getURL('shopping', 'Shopping_purchase_items_add')

        # Shopping - 采购项目 - 编辑
        self.Shopping_purchase_items_edit = self.shopping.getURL('shopping', 'Shopping_purchase_items_edit')

        # 3.token
        self.token = self.get_token()

        # 4. 创建请求对象
        self.R = RequestForHttp()

    # Shopping - 买家某个订单详情
    def Shopping_buyer_order_details_number_api(self, number):
        '''
        买家某个订单详情
        :param number : 订单号
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'number': number
        }

        # 2.替换id
        self.Shopping_buyer_order_details_number = self.Shopping_buyer_order_details_number.replace(":number", number)

        # 3.发送请求
        response = self.R.get_function(self.Shopping_buyer_order_details_number, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Shopping - 买家某个订单详情', url=self.Shopping_buyer_order_details_number, method='get')

        # 5.返回
        return response

    # Shopping - 买家订单-下单
    def Shopping_buyer_order_order_api(self, data):
        '''
        用户下单
        :param delivery_id      :   收货地址ID
        :param organization_id  :   卖家ID
        :param price_id         :   商品单价ID
        :param quantity         :   购买数量
        :param message          :   留言
        :param source_id        :   若是商城或协会下的产品加入的购物车，此处须传入商城或协会的team_id
        :return:
        '''
        # 0.定制请求头
        headers = {
            "Content-Type": "application/json"
        }

        data['token'] = self.token
        # data = {
        #     "token": self.token,
        #     "delivery_id": delivery_id,
        #     "groups": [{
        #         "message": message1,
        #         "organization_id": organization_id1,
        #         "items": [{
        #             "price_id": price_id1,
        #             "quantity": quantity1,
        #             "source_id": source_id1
        #         }]
        #     }, {
        #         "message": message2,
        #         "organization_id": organization_id2,
        #         "items": [{
        #             "price_id": price_id2,
        #             "quantity": quantity2,
        #             "source_id": source_id2
        #         }]
        #     }]
        # }

        # 2.将字典格式转化成json
        data = json.dumps(data)

        # 3.发送请求
        response = self.R.post_function(self.Shopping_buyer_order_order, data, headers=headers)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Shopping - 买家订单-下单', url=self.Shopping_buyer_order_order, method='post')

        # 5.返回
        return response

    # Shopping - 买家订单-列表
    def Shopping_buyer_order_list_api(self, number=None, state=None, item_state=None, page=None, per_page=None):
        '''
        获取指定用户的订单列表。(按照创建顺序倒序排列，最新下单的在前面)
        :param number       :   订单号 用来查询单一订单
        :param state        :   订单状态 根据此先进行订单状态过滤
                                submitted 待付款
                                paid 待发货
                                reminded 待发货(已提醒)
                                delivered 已发货
                                receipted 已收货
                                canceled 交易取消
                                finished 交易成功
                                settling 交易成功
                                settlement 交易成功
                                ['finished', 'receipted'] 待评论订单 (使用此状态时，item_state设置为['mounted', 'accepted', 'rejected'])
        :param item_state   :   订单中的商品状态 根据商品状态过滤 可选值有
                                submitted 待付款
                                mounted 支付完成
                                refunding 请求售后
                                accepted 同意售后
                                rejected 拒绝售后
                                commented 评论
        :param page         :   页数
        :param per_page     :   每页记录数
        :return:
        '''

        # 1.组装token和data
        data = {
            'token': self.token,
            'number': number,
            'state[]': state,
            'item_state': item_state,
            'page': page,
            'per_page': per_page
        }

        # 2.发送请求
        response = self.R.get_function(self.Shopping_buyer_order_list, data)

        # 3.打印日志
        self.plog.printlog(data, response, describle='Shopping - 买家订单-列表', url=self.Shopping_buyer_order_list, method='get')

        # 4.返回
        return response

    # Shopping - 买家订单-取消订单
    def Shopping_buyer_order_cancel_api(self, number):
        '''
        买家取消未支付的订单
        :param number   :   订单号
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'number': number
        }

        # 2.替换number
        self.Shopping_buyer_order_cancel = self.Shopping_buyer_order_cancel.replace(":number", number)

        # 3.发送请求
        response = self.R.put_function(self.Shopping_buyer_order_cancel, data)  # 当response为空时，此处返回status

        # 4.当response为空时，自动分配response返回值
        response_none = [response, '']

        # 5.打印日志
        self.plog.printlog(data, response_none, describle='Shopping - 买家订单-取消订单', url=self.Shopping_buyer_order_cancel, method='put')

        # 5.返回，此处结果为status码
        return response

    # Shopping - 买家订单-提醒发货
    def Shopping_buyer_order_remind_api(self, number):
        '''
        买家提醒发货
        :param number   :   订单号
        :return:
        '''

        # 1.准备数据
        data = {
            'token': self.token,
            'number': number
        }

        # 2.替换url中number
        self.Shopping_buyer_order_remind = self.Shopping_buyer_order_remind.replace(":number", number)

        # 3.发送请求
        response = self.R.put_function(self.Shopping_buyer_order_remind, data)

        # 4.替换结果，此处为put方法，返回结果为空
        response_none = [response, '']

        # 5.打印日志
        self.plog.printlog(data, response_none, describle='Shopping - 买家订单-提醒发货', url=self.Shopping_buyer_order_remind, method='put')

        # 6.返回，此处结果为status码
        return response


# 调试
shopping = Shopping()

# Shopping - 买家某个订单详情
# shopping.Shopping_buyer_order_details_number_api(number='121691026083027')

# Shopping - 买家订单-下单
# shopping.Shopping_buyer_order_order_single_api(delivery_id=245, organization_id=4835, price_id=63363, quantity=1)


# Shopping - 买家订单-下单-多订单
# data = {
#     "token": "41d956f78205b4f0f787a54bd44fed74",
#     "delivery_id": 245,
#     "groups": [{
#         "message": "，测",
#         "organization_id": 5556,
#         "items": [{
#             "price_id": 63372,
#             "quantity": 1
#         }]
#     }, {
#         "message": "，测",
#         "organization_id": 4835,
#         "items": [{
#             "price_id": 62612,
#             "quantity": 1
#         }]
#     }]
# }
# shopping.Shopping_buyer_order_order_more_api(data)

# Shopping - 买家订单-列表
# shopping.Shopping_buyer_order_list_api(state='submitted')

# Shopping - 买家订单-取消订单
# shopping.Shopping_buyer_order_cancel_api(number='121750892001309')

# Shopping - 买家订单-提醒发货
# shopping.Shopping_buyer_order_remind_api(number='121751027503208')
