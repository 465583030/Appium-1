# Author:# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.api.TeamConstruction import *


# Space
@ddt.ddt
class TeamConstruction(Login):
    def __init__(self):
        Handle.__init__(self)


        # 1. 创建读取配置信息对象
        self.team_construction = GlobalParam('config', 'team_construction.conf')

        # 2.接口路由
        # Team_Construction - 业务列表
        self.Team_Construction_business_list = self.team_construction.getURL('team_construction', 'Team_Construction_business_list')

        # Team_Construction - 业务开启
        self.Team_Construction_business_open = self.team_construction.getURL('team_construction', 'Team_Construction_business_open')

        # Team_Construction - 产业角色-修改
        self.Team_Construction_industry_modify = self.team_construction.getURL('team_construction', 'Team_Construction_industry_modify')

        # Team_Construction - 员工主动退出
        self.Team_Construction_employee_quit = self.team_construction.getURL('team_construction', 'Team_Construction_employee_quit')

        # Team_Construction - 员工任免
        self.Team_Construction_employee_assign = self.team_construction.getURL('team_construction', 'Team_Construction_employee_assign')

        # Team_Construction - 员工列表
        self.Team_Construction_employee_list = self.team_construction.getURL('team_construction', 'Team_Construction_employee_list')

        # Team_Construction - 员工新增-邀请
        self.Team_Construction_employee_add = self.team_construction.getURL('team_construction', 'Team_Construction_employee_add')

        # Team_Construction - 员工移除
        self.Team_Construction_employee_delete = self.team_construction.getURL('team_construction', 'Team_Construction_employee_delete')

        # Team_Construction - 导购名额开关-切换
        self.Team_Construction_quota_switch = self.team_construction.getURL('team_construction', 'Team_Construction_quota_switch')

        # Team_Construction - 是否是团队员工
        self.Team_Construction_is_joined = self.team_construction.getURL('team_construction', 'Team_Construction_is_joined')

        # Team_Construction - 机构成员列表
        self.Team_Construction_members_list = self.team_construction.getURL('team_construction', 'Team_Construction_members_list')

        # Team_Construction - 模块权限
        self.Team_Construction_can_do = self.team_construction.getURL('team_construction', 'Team_Construction_can_do')

        # Team_Construction - 职位列表
        self.Team_Construction_groups_list = self.team_construction.getURL('team_construction', 'Team_Construction_groups_list')

        # Team_Construction - 职位更新
        self.Team_Construction_groups_update = self.team_construction.getURL('team_construction', 'Team_Construction_groups_update')

        # Team_Construction - 职位申请-处理
        self.Team_Construction_groups_application = self.team_construction.getURL('team_construction', 'Team_Construction_groups_application')

        # Team_Construction - 职位详情
        self.Team_Construction_groups_detail = self.team_construction.getURL('team_construction', 'Team_Construction_groups_detail')

        # Team_Construction - 部门列表
        self.Team_Construction_departments_list = self.team_construction.getURL('team_construction', 'Team_Construction_departments_list')

        # Team_Construction - 部门列表(我的部门)
        self.Team_Construction_departments_mine = self.team_construction.getURL('team_construction', 'Team_Construction_departments_mine')

        # Team_Construction - 部门更新
        self.Team_Construction_departments_update = self.team_construction.getURL('team_construction', 'Team_Construction_departments_update')

        # 3.token
        self.token = self.get_token()

        # 4. 创建请求对象
        self.R = RequestForHttp()

    """
      @api {get} /api/v1/team/:team_id/packages 业务列表
      @apiGroup Team Construction
      @apiName packages
      @apiDescription 获取指定团队的可用业务列表。(1.该接口需要业务的浏览权限:后台管理配置);(2.用于机构空间业务升级列表)

      @apiParam {String} token
      @apiParam {Number} team_id 团队ID

      @apiParamExample {json} Request-Example:
      {
        'token': 'e156d8f635eaa66230368130ed207579', 
        'team_id': '4835'
      }

      @apiSuccess (200) {Object[]} packages 业务
      @apiSuccess (200) {Number} packages.id 业务ID
      @apiSuccess (200) {String} packages.name 业务名称
      @apiSuccess (200) {String} packages.alias 业务别名
      @apiSuccess (200) {String[]} packages.status 业务状态 not-enabled：未开启；enabled：已开启；disabled：不可用
      @apiSuccess (200) {String} packages.description 业务描述
      @apiSuccess (403) {String} message 错误信息 用户没有浏览业务权限
      
      @apiSuccessExample {json} Success-Response:
       HTTP/1.1 200 OK
       [
        {
            "alias": "inner_guide",
            "description": "所有员工都能通过自己的人脉帮助企业获取更多的客户资源",
            "enable": true,
            "id": 10,
            "name": "企业内部全员销售",
            "status": [
                "enabled"
            ]
        },
        {
            "alias": "outer_guide",
            "description": null,
            "enable": true,
            "id": 11,
            "name": "企业外部导购",
            "status": [
                "enabled",
                "disabled"
            ]
        },
        {
            "alias": "set_target_customer",
            "description": "定制企业客户可以帮助企业精准找到下游客户。",
            "enable": false,
            "id": 14,
            "name": "定制企业客户",
            "status": [
                "not-enabled"
            ]
        },
        {
            "alias": "dianshang",
            "description": "企业电商",
            "enable": true,
            "id": 5,
            "name": "自助电商",
            "status": [
                "enabled"
            ]
        },
        {
            "alias": "tuandui",
            "description": "团队协作",
            "enable": true,
            "id": 6,
            "name": "团队协作",
            "status": [
                "enabled"
            ]
        }
       ]
    
    """

    # Team_Construction - 业务列表
    def Team_Construction_business_list_api(self, team_id):
        '''
        获取指定团队的可用业务列表。（该接口需要业务的浏览权限）
        :param team_id : 团队ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id
        }

        # 2.替换id
        self.Team_Construction_business_list = self.Team_Construction_business_list.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_business_list, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 业务列表', url=self.Team_Construction_business_list, method='get')

        # 5.返回
        return response

        # Team_Construction - 业务列表

    """
     @api {put} /api/v1/team/4835/packages/6 业务开启(业务升级)
     @apiGroup Team Construction
     @apiName update_packages
     @apiDescription 当前团队开启指定业务。(该接口需要业务的更新权限，常用于机构空间业务升级中)

     @apiParam {String} token
     @apiParam {Number} team_id 团队ID
     @apiParam {Number} id 业务ID

     @apiParamExample {json} Request-Example:
     {
        'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
        'team_id': '4835', 
        'id': '6'
     }

     @apiSuccess (200) {String}  success 成功状态
     @apiSuccess (403) {String} message 错误信息 用户没有更新业务权限

     @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
      {
          "success": true
      }

    """

    # Team_Construction - 业务开启
    def Team_Construction_business_open_api(self, team_id, id):
        '''
        当前团队开启指定业务。（该接口需要业务的更新权限）
        :param team_id : 团队ID
        :param id      : 业务ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'id': id
        }

        # 2.替换id
        self.Team_Construction_business_open = self.Team_Construction_business_open.replace(":id", id)
        self.Team_Construction_business_open = self.Team_Construction_business_open.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.put_function(self.Team_Construction_business_open, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 业务开启', url=self.Team_Construction_business_open, method='put')

        # 5.返回
        return response

    """
        Team_Construction - 产业角色 - 修改：没有此功能了(不能修改产业角色前端)
    """

    # Team_Construction - 产业角色 - 修改(未使用)
    def Team_Construction_industry_modify_api(self, team_id, server_id):
        '''
        修改企业的产业角色，定制企业上下游
        :param team_id   : 团队ID
        :param server_id : 新的产业角色id
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'server_id': server_id
        }

        # 2.替换id
        self.Team_Construction_industry_modify = self.Team_Construction_industry_modify.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.put_function(self.Team_Construction_industry_modify, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 产业角色-修改', url=self.Team_Construction_industry_modify, method='put')

        # 5.返回
        return response

    """
     @api {delete} /api/v1/team/:team_id/users/quit 员工主动退出团队
     @apiGroup Team Construction
     @apiName quit_team
     @apiDescription 员工主动退出团队(常用于机构空间退出团队)

     @apiParam {String} token
     @apiParam {Number} team_id 团队ID

     @apiParamExample {json} Request-Example:
     {
        'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
        'team_id': '5712'
     }

     @apiSuccess (200) {Boolean}  success 操作成功
     @apiSuccess (4XX) {Boolean} success 操作失败
     @apiSuccess (4XX) {String} msg 操作失败信息

     @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
      {
          "success": true
      }

    """

    # Team_Construction - 员工主动退出
    def Team_Construction_employee_quit_api(self, team_id):
        '''
        员工主动退出团队(常用于机构空间退出团队)
        :param team_id   : 团队ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
        }

        # 2.替换id
        self.Team_Construction_employee_quit = self.Team_Construction_employee_quit.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.delete_function(self.Team_Construction_employee_quit, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 员工主动退出', url=self.Team_Construction_employee_quit, method='delete')

        # 5.返回
        return response

    """
        @api {put} /api/v1/team/:team_id/users/:id 员工职位任免
        @apiGroup Team Construction
        @apiName move_users
        @apiDescription 员工任免指定职位。(该接口需要员工的更新权限，常用于机构空间团队职位任免中)
    
        @apiParam {String} token
        @apiParam {Number} team_id 团队ID
        @apiParam {Number} id 员工ID
        @apiParam {Number[]} groups_ids 分配的职位ID
        
    
        @apiParamExample {json} Request-Example:
        {
            'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
            'team_d': '4835', 
            'group_dis[]': '44', 
            'id': '5de2ab00-f4f4-4d4a-8641-076e58a6492e'
        }
    
        @apiSuccess (200) {String}  success  成功状态
        @apiSuccess (200) {Number}  group_ids 操作成功的职位ID
        @apiSuccess (4XX) {String} msg 操作失败信息
    
        @apiSuccessExample {json} Success-Response:
         HTTP/1.1 200 OK
         {
            "group_ids": [
                215,
                44,
                90,
                86,
                87,
                25,
                25,
                25
            ],
            "success": true
         }

    """

    # Team_Construction - 员工任免
    def Team_Construction_employee_assign_api(self, team_id, id, group_ids):
        '''
        员工任免指定职位。（该接口需要员工的更新权限）
        :param team_id   :  团队ID
        :param id        :  员工ID
        :param group_ids :  分配的职位ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_d': team_id,
            'group_dis[]': group_ids,
            'id': id
        }

        # 2.替换id
        self.Team_Construction_employee_assign = self.Team_Construction_employee_assign.replace(":id", id)
        self.Team_Construction_employee_assign = self.Team_Construction_employee_assign.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.put_function(self.Team_Construction_employee_assign, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 员工任免', url=self.Team_Construction_employee_assign, method='put')

        # 5.返回
        return response

    """
       @api {get} /api/v1/team/:team_id/users 员工列表
       @apiGroup Team Construction
       @apiName users
       @apiDescription 获取指定团队的员工列表。（该接口需要员工的浏览权限,常用于团队人员列表，可查询部门员工、职位员工、模糊查询员工)

       @apiParam {String} token
       @apiParam {Number} team_id 团队ID
       @apiParam {Number[]} [groups_ids] 职位ID 提供该值则返回该职位的员工
       @apiParam {Number[]} [dept_ids] 部门ID 提供该值则返回该部门的员工
       @apiParam {String} [q] 查询字符串，模糊查询，不提供该值则返回所有员工

       @apiParamExample {json} Request-Example:
       {
            'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
            'team_d': '4835', 
            'group_dis[]': None, 
            'dept_ids[]': None, 
            'q': None
       }

       @apiSuccess (200) {Object[]} users 员工
       @apiSuccess (200) {Number} users.id 员工ID
       @apiSuccess (200) {String} users.name 员工姓名
       @apiSuccess (200) {Object[]} users.groups 员工职位
       @apiSuccess (200) {Number} users.groups.id 职位ID
       @apiSuccess (200) {String} users.groups.name 职位名称
       @apiSuccess (200) {String} users.groups.alias 职位别名
       @apiSuccess (200) {String} users.groups.clients_count 客户数 职位别名为outer_guide时存在该参数
       
       @apiSuccess (403) {String} message 错误信息 用户没有浏览员工权限

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        [
            {
                "groups": [],
                "id": "5de2ab00-f4f4-4d4a-8641-076e58a6492e",
                "name": "祝菲"
            }
        ]

   """

    # Team_Construction - 员工列表
    def Team_Construction_employee_list_api(self, team_id, group_ids=None, dept_ids=None, q=None):
        '''
        获取指定团队的员工列表。（该接口需要员工的浏览权限）
        :param team_id   :  团队ID
        :param group_ids :  职位ID 提供该值则返回该职位的员工
        :param dept_ids  :  部门ID 提供该值则返回该部门的员工
        :param q         :  查询字符串，模糊查询，不提供该值则返回所有员工
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_d': team_id,
            'group_dis[]': group_ids,
            'dept_ids[]': dept_ids,
            'q': q,
        }

        # 2.替换id
        self.Team_Construction_employee_list = self.Team_Construction_employee_list.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_employee_list, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 员工列表', url=self.Team_Construction_employee_list, method='get')

        # 5.返回
        return response

    """
       @api {post} /api/v1/team/:team_id/users 员工新增-邀请
       @apiGroup Team Construction
       @apiName invite_stranger
       @apiDescription 获取指定团队的员工列表。（该接口需要员工的浏览权限,常用于团队人员列表，可查询部门员工、职位员工、模糊查询员工)

       @apiParam {String} token
       @apiParam {Number} team_id 团队ID
       @apiParam {Number[]} stranger_ids 联系人ID

       @apiParamExample {json} Request-Example:
       {
            'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
            'team_id': '4835', 
            'stranger_ids[]': '183262'
       }

       @apiSuccess {String} success 成功状态
       @apiSuccess {Number[]} stranger_ids 操作成功的联系人ID
       @apiSuccess {Object[]} sms_strangers 需要发送短信的联系人
       @apiSuccess {String} sms_strangers.mobile 联系人手机号
       @apiSuccess {String} sms_content 短信内容

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "sms_content": "肖静远邀请您加入测试机构企业空间。下载 http://www.360stones.com/qrcode",
            "sms_strangers": [],
            "stranger_ids": [
                183262
            ],
            "success": true
        }

   """

    # Team_Construction - 员工新增-邀请
    def Team_Construction_employee_add_api(self, team_id, stranger_ids):
        '''
        添加若干联系人为员工，并指派一个职位。（该接口需要员工的新增权限,已改为发出邀请-员工接受邀请）
        :param team_id          :  团队ID
        :param stranger_ids     :  联系人ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_d': team_id,
            'stranger_ids[]': stranger_ids
        }

        # 2.替换id
        self.Team_Construction_employee_add = self.Team_Construction_employee_add.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.post_function(self.Team_Construction_employee_add, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 员工新增-邀请', url=self.Team_Construction_employee_add, method='post')

        # 5.返回
        return response

    """
       @api {delete} /api/v1/team/:team_id/users 员工移除
       @apiGroup Team Construction
       @apiName delete_users
       @apiDescription 从当前团队移除指定的员工。（该接口需要员工的删除权限,常用于团队中移除某员工）

       @apiParam {String} token
       @apiParam {Number} team_id 团队ID
       @apiParam {Number[]} user_ids 员工ID

       @apiParamExample {json} Request-Example:
       {
            'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
            'team_d': '4835', 
            'user_ids[]': 'd66dcb63-107f-4d30-a632-d97882b7465f'
       }

       @apiSuccess {String[]} user_ids 操作成功的员工ID

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "user_ids": [
                "d66dcb63-107f-4d30-a632-d97882b7465f"
            ]
        }

    """

    # Team_Construction - 员工移除
    def Team_Construction_employee_delete_api(self, team_id, user_ids):
        '''
        从当前团队移除指定的员工。（该接口需要员工的删除权限）
        :param team_id          :  团队ID
        :param user_ids         :  员工ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'user_ids[]': user_ids
        }

        # 2.替换id
        self.Team_Construction_employee_delete = self.Team_Construction_employee_delete.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.delete_function(self.Team_Construction_employee_delete, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 员工移除', url=self.Team_Construction_employee_delete, method='delete')

        # 5.返回
        return response

    """
       @api {put} /api/v1/team/:team_id/quota_switch 导购名额开关-切换
       @apiGroup Team Construction
       @apiName quota_switch
       @apiDescription 修改当前企业是否允许开放导购名额

       @apiParam {String} token
       @apiParam {Number} team_id 团队ID
       @apiParam {String} event on打开，off关闭

       @apiParamExample {json} Request-Example:
       {
            'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
            'team_id': '4835', 
            'event': 'off'
       }

       @apiSuccess {Boolean} success  操作成功

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "success": true
        }

    """

    # Team_Construction - 导购名额开关-切换
    def Team_Construction_quota_switch_api(self, team_id, event):
        '''
        修改当前企业是否允许开放导购名额
        :param team_id          :  团队ID
        :param event            :  员工ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'event': event
        }

        # 2.替换id
        self.Team_Construction_quota_switch = self.Team_Construction_quota_switch.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.put_function(self.Team_Construction_quota_switch, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 导购名额开关-切换', url=self.Team_Construction_quota_switch, method='put')

        # 5.返回
        return response

    """
       @api {get} /api/v1/team/:team_id/users/joined 是否是团队员工
       @apiGroup Team Construction
       @apiName joined_team
       @apiDescription 判断当前用户是否是某个团队的员工

       @apiParam {String} token
       @apiParam {Number} team_id 团队ID

       @apiParamExample {json} Request-Example:
       {
            'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
            'team_id': '4835'
       }

       @apiSuccess {Boolean} is_joined 操作成功

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "is_joined": true
        }
    """

    # Team_Construction - 是否是团队员工
    def Team_Construction_is_joined_api(self, team_id):
        '''
        是否是团队员工
        :param team_id          :  团队ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
        }

        # 2.替换id
        self.Team_Construction_is_joined = self.Team_Construction_is_joined.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_is_joined, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 是否是团队员工', url=self.Team_Construction_is_joined, method='get')

        # 5.返回
        return response

    """
       @api {get} /api/v1/team/:team_id/members 机构成员列表
       @apiGroup Team Construction
       @apiName team_members
       @apiDescription 获取指定机构的成员列表。（该接口需要员工的浏览权限，常用于查询协会/商城的会员列表）

       @apiParam {String} token
       @apiParam {Number} team_id 机构ID
       @apiParam {String} [q] 查询字符串，模糊查询，不提供该值则返回所有成员
       @apiParam {String[]} [states] 状态
                                    <ul>
                                    <li>submitted 待审核</li>
                                    <li>invitee 已邀请</li>
                                    <li>accepted 已审核</li>
                                    <li>rejected 拒绝申请</li>
                                    <li>reject_invited 拒绝邀请</li>
                                    </ul>

       @apiParamExample {json} Request-Example:
       {
           'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
           'team_id': '5029', 
           'q': None, 'states[]': None, 
           'page': None, 
           'per_page': None
       }

       @apiSuccess {Object[]} preps 成员
       @apiSuccess {Number} preps.id 申请/邀请信息ID
       @apiSuccess {String="submitted", "invited", "accepted", "rejected", "reject_invited"} state 状态
                                    <ul>
                                    <li>待审核</li>
                                    <li>已邀请</li>
                                    <li>已审核</li>
                                    <li>拒绝申请</li>
                                    <li>拒绝邀请</li>
                                    </ul>
        @apiSuccess {Object} preps.user 成员用户信息 
        @apiSuccess {String} preps.user.id 用户ID 
        @apiSuccess {String} preps.user.name 姓名 
        @apiSuccess {String} preps.user.avatar_url 头像 
        
        @apiSuccess {Object[]} meta 
        @apiSuccess {Number} meta.page_size 每页记录数 
        @apiSuccess {Number} meta.total 记录总数 
        @apiSuccess {Number} meta.all_total 全部的成员总数，此以下四项当q为空的时候才返回
        @apiSuccess {Number} meta.invited_total 已邀请总数
        @apiSuccess {Number} meta.accepted_total 已通过
        @apiSuccess {Number} meta.submitted_total 待确认

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
        "meta": {
            "accepted_total": 1,
            "all_total": 2,
            "invited_total": 1,
            "page_size": 10,
            "submitted_total": 0,
            "total": 2
        },
        "preps": [
            {
                "id": 7957,
                "state": "accepted",
                "user": {
                    "avatar_url": "http://7xjfsp.com1.z0.glb.clouddn.com/ll3ON6AthUd03YektGlnqtQBUPJB-thumb",
                    "id": "20d7338a-3dee-426a-9e3d-33305b8bae83",
                    "name": "张梦"
                }
            },
            {
                "id": 7956,
                "state": "invited",
                "user": {
                    "avatar_url": "http://7xjfsp.com1.z0.glb.clouddn.com/Flkm9wlL1sx7-xDDNr1VXved8P4P-thumb",
                    "id": "6d63a58e-5e18-4419-8670-1bebae402642",
                    "name": "皇宫"
                }
            }
        ]
        }
    """

    # Team_Construction - 机构成员列表
    def Team_Construction_members_list_api(self, team_id, q=None, states=None, page=None, per_page=None):
        '''
        获取指定机构的成员列表。（该接口需要员工的浏览权限）
        :param team_id          :  团队ID
        :param q                :  查询字符串，模糊查询，不提供该值则返回所有成员
        :param states           :  状态
                                    submitted 待审核
                                    invitee 已邀请
                                    accepted 已审核
                                    rejected 拒绝申请
                                    reject_invited 拒绝邀请
        :param page             :  页数
        :param per_page         :  每页记录数

        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'q': q,
            'states[]': states,
            'page': page,
            'per_page': per_page
        }

        # 2.替换id
        self.Team_Construction_members_list = self.Team_Construction_members_list.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_members_list, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 机构成员列表', url=self.Team_Construction_members_list, method='get')

        # 5.返回
        return response

    """
       @api {get} /api/v1/team/:team_id/can_do 模块权限
       @apiGroup Team Construction
       @apiName can_do
       @apiDescription 获取指定模块的权限

       @apiParam {String} token
       @apiParam {Number} team_id 团队ID
       @apiParam {String[]="read", "update"} [Group] 职位的权限 <br>read-浏览; update-编辑;
       @apiParam {String[]="read", "update"} [Organization] 企业信息的权限 <br>read-浏览; update-编辑;
       @apiParam {String[]="read", "update"} [Department] 部门的权限 <br>read-浏览; update-编辑;
       @apiParam {String[]="read", "update"} [EnablePackage] 业务 <br>read-浏览; update-编辑;
       @apiParam {String[]="read", "create", "update", "destroy"} [Team] 员工 <br>read-浏览; create-新增; update-任免; destroy-移除;
       @apiParam {String[]="read", "create", "update", "destroy"} [Product] 产品 <br>read-浏览; create-新增; update-更新; destroy-删除; publish-发布; recall-撤回;
       @apiParam {String[]="read", "create", "update", "destroy","publish", "recall"} [Archive] 产品 <br>read-浏览; create-新增; update-更新; destroy-删除; publish-发布; recall-撤回;
       @apiParam {String[]="read", "create", "destroy"} [Photo] 图片 <br>read-浏览; create-上传; destroy-删除;

       @apiParamExample {json} Request-Example:
       {
            'token': 'd0dbcb9a2b3dbb24008c1ab0dfdc3c93', 
            'team_id': '4835', 
            'Group': None, 
            'Organization': None, 
            'Department': None, 
            'EnablePackage': None, 
            'Team': None, 
            'Product': None, 
            'Archive': None, 
            'Photo': None
        }

       @apiSuccess {Object[]} preps 成员
       @apiSuccess {Number} preps.id 申请/邀请信息ID
       @apiSuccess {String="submitted", "invited", "accepted", "rejected", "reject_invited"} state 状态
                                    <ul>
                                    <li>待审核</li>
                                    <li>已邀请</li>
                                    <li>已审核</li>
                                    <li>拒绝申请</li>
                                    <li>拒绝邀请</li>
                                    </ul>
        @apiSuccess {Object} preps.user 成员用户信息 
        @apiSuccess {String} preps.user.id 用户ID 
        @apiSuccess {String} preps.user.name 姓名 
        @apiSuccess {String} preps.user.avatar_url 头像 

        @apiSuccess {Object[]} meta 
        @apiSuccess {Number} meta.page_size 每页记录数 
        @apiSuccess {Number} meta.total 记录总数 
        @apiSuccess {Number} meta.all_total 全部的成员总数，此以下四项当q为空的时候才返回
        @apiSuccess {Number} meta.invited_total 已邀请总数
        @apiSuccess {Number} meta.accepted_total 已通过
        @apiSuccess {Number} meta.submitted_total 待确认

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
        "Archive": {
            "create": true,
            "destroy": true,
            "publish": true,
            "read": true,
            "recall": true,
            "update": true
        },
        "Client": {
            "admin": true,
            "create": true,
            "destroy": true,
            "read": true,
            "update": true
        },
        "ClientKeyword": {
            "read": true
        },
        "Department": {
            "read": true,
            "update": true
        },
        "EnablePackage": {
            "read": true,
            "update": true
        },
        "Group": {
            "read": true,
            "update": true
        },
        "Guild": {
            "create": true,
            "destroy": true,
            "update": true
        },
        "OrderForm": {
            "read": true,
            "update": true
        },
        "Organization": {
            "destroy": true,
            "read": true,
            "update": true
        },
        "Photo": {
            "create": true,
            "destroy": true,
            "read": true
        },
        "Product": {
            "audit": true,
            "create": true,
            "destroy": true,
            "publish": true,
            "read": true,
            "recall": true,
            "update": true
        },
        "Team": {
            "create": true,
            "destroy": true,
            "read": true,
            "update": true
        },
        "Visit": {
            "read": false
        }
    }
    """

    # Team_Construction - 模块权限
    def Team_Construction_can_do_api(self, team_id, Group=None, Organization=None,
                                     Department=None, EnablePackage=None, Team=None,
                                     Product=None, Archive=None, Photo=None):
        '''
        获取指定机构的成员列表。（该接口需要员工的浏览权限）
        :param team_id          :  团队ID
        :param Group            :  职位的权限
                                   read-浏览; update-编辑;
                                   允许值: "read", "update"
        :param Organization     :  企业信息的权限
                                   read-浏览; update-更新;
                                   允许值: "read", "update"
        :param Department       :  部门的权限
                                   read-浏览; update-编辑;
                                   允许值: "read", "update"
        :param EnablePackage    :  业务
                                   read-浏览; update-开启;
                                   允许值: "read", "update"
        :param Team             :  员工
                                   read-浏览; create-新增; update-任免; destroy-移除;
                                   允许值: "read", "create", "update", "destroy"
        :param Product          :  产品
                                   read-浏览; create-新增; update-更新; destroy-删除; publish-发布; recall-撤回;
                                   允许值: "read", "create", "update", "destroy", "publish", "recall"
        :param Archive          :  公司档
                                   read-浏览; create-新增; update-更新; destroy-删除; publish-发布; recall-撤回;
                                   允许值: "read", "create", "update", "destroy", "publish", "recall"
        :param Photo            :  图片
                                   read-浏览; create-上传; destroy-删除;
                                   允许值: "read", "create", "destroy"
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'Group': Group,
            'Organization': Organization,
            'Department': Department,
            'EnablePackage': EnablePackage,
            'Team': Team,
            'Product': Product,
            'Archive': Archive,
            'Photo': Photo
        }

        # 2.替换id
        self.Team_Construction_can_do = self.Team_Construction_can_do.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_can_do, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 模块权限', url=self.Team_Construction_can_do, method='get')

        # 5.返回
        return response

    """
      @api {get} /api/v1/team/:team_id/members 职位列表
      @apiGroup Team Construction
      @apiName groups
      @apiDescription 获取指定团队下指定部门的职位列表。（该接口需要职位的浏览权限）

      @apiParam {String} token
      @apiParam {Number} team_id 团队ID
      @apiParam {Number} dept_id 部门ID

      @apiParamExample {json} Request-Example:
      {
        'token': 'e4423f326ab0a7f7fc64c08689ee403d', 
        'team_id': '4835', 
        'dept_id': '9'
      }

      @apiSuccess (200) {Object[]} groups 职位
      @apiSuccess (200) {Number} groups.id 职位ID
      @apiSuccess (200) {String} groups.name 职位名称
      @apiSuccess (200) {Number} groups.quota 职位名额
      @apiSuccess (200) {String} groups.clazz 职位类型 master-负责人 normal-普通
      @apiSuccess (200) {Number} groups.user_count 职位员工数
      @apiSuccess (200) {Number} groups.dept_id 所属部门
        
      @apiSuccess (403) {String} message 错误信息 用户没有职位浏览权限
        
      @apiSuccessExample {json} Success-Response:
       HTTP/1.1 200 OK
       [
            {
                "clazz": "master",
                "id": 18,
                "name": "管理员",
                "quota": 1,
                "user_count": 1
            }
       ]
   """

    # Team_Construction - 职位列表
    def Team_Construction_groups_list_api(self, team_id, dept_id):
        '''
        获取指定团队下指定部门的职位列表。（该接口需要职位的浏览权限）
        :param team_id      :   团队ID
        :param dept_id      :   部门ID
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'dept_id': dept_id
        }

        # 2.替换id
        self.Team_Construction_groups_list = self.Team_Construction_groups_list.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_groups_list, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 机构成员列表', url=self.Team_Construction_groups_list, method='get')

        # 5.返回
        return response

    """
      @api {get} /api/v1/team/:team_id/members 职位更新
      @apiGroup Team Construction
      @apiName update_group
      @apiDescription 更新指定团队的指定职位。（该接口需要职位的更新权限）(常用于更新某职位人数)

      @apiParam {String} token
      @apiParam {Number} team_id 团队ID
      @apiParam {Number} id 职位ID
      @apiParam {Number} [quota] 职位名额

      @apiParamExample {json} Request-Example:
      {
          'token': 'e4423f326ab0a7f7fc64c08689ee403d', 
          'team_id': '4835', 
          'id': '18', 
          'quota': '2'
      }

      @apiSuccess (200) {String} success 成功状态
      @apiSuccess (403) {String} message 错误信息 用户没有职位更新权限

      @apiSuccessExample {json} Success-Response:
       HTTP/1.1 200 OK
       {
            "success": true
       }
    """

    # Team_Construction - 职位更新
    def Team_Construction_groups_update_api(self, team_id, id, quota=None):
        '''
        更新指定团队的指定职位。（该接口需要职位的更新权限）
        :param team_id      :   团队ID
        :param id           :   职位ID
        :param quota        :   职位名额
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'id': id,
            'quota': quota
        }

        # 2.替换id
        self.Team_Construction_groups_update = self.Team_Construction_groups_update.replace(":team_id", team_id)
        self.Team_Construction_groups_update = self.Team_Construction_groups_update.replace(":id", id)

        # 3.发送请求
        response = self.R.put_function(self.Team_Construction_groups_update, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 职位更新', url=self.Team_Construction_groups_list, method='put')

        # 5.返回
        return response

    """
      @api {put} /api/v1/team/:team_id/members 职位申请-处理
      @apiGroup Team Construction
      @apiName members_update
      @apiDescription 当前机构处理用户的会员申请（该接口需要员工的新增权限）

      @apiParam {String} token
      @apiParam {Number} team_id 团队ID
      @apiParam {Number[]} ids 邀请信息ID，数组形式
      @apiParam {String="accept","reject"} [event] 状态变化 accept-接受 reject-拒绝

      @apiParamExample {json} Request-Example:
      {
        'token'	: 'e4423f326ab0a7f7fc64c08689ee403d'
        'event'	: 'accept'
        'team_id' : '4835'
        'ids[]'	: '10736'
      }

      @apiSuccess (200) {Object[]} pms 操作失败的邀请信息
      @apiSuccess (200) {Number} pms.id 邀请信息ID
      @apiSuccess (200) {String} pms.msg 信息
      
      @apiSuccess (403) {Number} code 错误码
      @apiSuccess (403) {String} detail 当前状态不正确
        
      @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
       {
            "pms": []       
       }
    """

    # Team_Construction - 职位申请-处理
    def Team_Construction_groups_application_api(self, team_id, ids, event=None):
        '''
        当前机构处理用户的会员申请（该接口需要员工的新增权限）
        :param team_id      :   团队ID
        :param ids          :   邀请信息ID, 数组形式
        :param event        :   状态变化 accept-接受 reject-拒绝
                                允许值: "accept", "reject"
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'ids[]': ids,
            'event': event
        }

        # 2.替换id
        self.Team_Construction_groups_application = self.Team_Construction_groups_application.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.put_function(self.Team_Construction_groups_application, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 职位申请-处理', url=self.Team_Construction_groups_application, method='put')

        # 5.返回
        return response

    """
      @api {get} /api/v1/team/:team_id/groups/detail 职位详情
      @apiGroup Team Construction
      @apiName detail_group
      @apiDescription 获取指定团队的指定职位详情。（该接口需要职位的浏览权限）常用于获取导购员职位的职位详情信息

      @apiParam {String} token
      @apiParam {Number} team_id      团队ID
      @apiParam {Number} [role_id]    职位ID 未提供该参数时，需要提供 role_alias
      @apiParam {String} [role_alias] 职位别名 未提供该参数时，需要提供 role_id， outer_guide-导购员
    
      @apiParamExample {json} Request-Example:
      {
          'token': 'e4423f326ab0a7f7fc64c08689ee403d', 
          'team_id': '4835', 
          'role_id': None, 
          'role_alias': 'outer_guide'
      }

      @apiSuccess (200) {Object[]} groups 职位
      @apiSuccess (200) {Number} groups.id 职位ID
      @apiSuccess (200) {String} groups.name 职位名称
      @apiSuccess (200) {Number} groups.quota 职位名额
      @apiSuccess (200) {Number} groups.user_count 职位已就职人数
      @apiSuccess (200) {String} groups.clazz 职位类型 master-负责人 normal-普通
      @apiSuccess (200) {String} groups.String 职位别名
      @apiSuccess (200) {String} groups.description 职位描述

      @apiSuccess (200) {Object[]} guide_terms 导购协议 职位别名为outer_guide时存在该参数
      @apiSuccess (200) {Number} guide_terms.id 导购协议ID
      @apiSuccess (200) {Number} guide_terms.rate 导购提成
      @apiSuccess (200) {Number} guide_terms.period 导购有效期
      @apiSuccess (200) {Number} guide_terms.period 导购有效期
      @apiSuccess (200) {Number} guide_terms.put_date 提成发放日

      @apiSuccess (403) {Number} code 错误码
      @apiSuccess (403) {String} detail 无浏览权限，内容为“试图访问受限资源”

      @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
       {
        "groups": [
            {
                "alias": null,
                "clazz": "outer",
                "description": "<p>1. 努力提高自身的知名度、信用度、美誉度，维护好自身光辉形象。 </p>\n<p>2. 利用自己的人脉资源,通过各种分享和传播渠道，帮助企业添加有效客户。</p>\n<p>3. 与客户保持良好沟通，提高企业在客户中的口碑。</p>",
                "id": 7086,
                "name": "导购员",
                "quota": 0,
                "user_count": 0
            }
        ],
        "guide_terms": [
            {
                "age": null,
                "end_date": "2020-04-19",
                "gender": null,
                "id": 227,
                "link_number": null,
                "organization_id": 4835,
                "period": 3,
                "put_date": 5,
                "rate": 1.0,
                "requirements": null,
                "responsibilities": null,
                "start_date": "2017-04-19",
                "state": "editing"
            }
        ]
    }

    """

    # Team_Construction - 职位详情
    def Team_Construction_groups_detail_api(self, team_id, role_id=None, role_alias=None):
        '''
        获取指定团队的指定职位详情。（该接口需要职位的浏览权限）
        :param team_id         :   团队ID
        :param role_id         :   职位ID 未提供该参数时，需要提供 role_alias
        :param role_alias      :   职位别名 未提供该参数时，需要提供 role_id， outer_guide-导购员
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'role_id': role_id,
            'role_alias': role_alias
        }

        # 2.替换id
        self.Team_Construction_groups_detail = self.Team_Construction_groups_detail.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_groups_detail, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 职位详情', url=self.Team_Construction_groups_detail, method='get')

        # 5.返回
        return response

    """
      @api {get} /api/v1/team/:team_id/departments 部门列表
      @apiGroup Team Construction
      @apiName departments
      @apiDescription 获取指定团队的部门列表。（该接口需要部门的浏览权限）

      @apiParam {String} token
      @apiParam {Number} team_id        团队ID
      @apiParam {Boolean} [has_groups]  是否附加该部门的职位列表。（如提供该参数则该接口还需拥有职位的浏览权限）  
      @apiParam {Boolean} [ex] 职位别名  为true时，则排除掉导购员职位

      @apiParamExample {json} Request-Example:
      {
          'token': 'e4423f326ab0a7f7fc64c08689ee403d', 
          'team_id': '4835', 
          'has_groups': 'true', 
          'ex': None
      }

      @apiSuccess (200) {Object[]} departments 部门
      @apiSuccess (200) {Object[]} departments.groups 职位
      @apiSuccess (200) {Number} departments.groups.id 职位ID
      @apiSuccess (200) {String} departments.groups.name 职位名称
      @apiSuccess (200) {Number} departments.groups.quota 名额
      @apiSuccess (200) {String} departments.groups.clazz 职位类型 master-负责人 normal-普通
      @apiSuccess (200) {Number} departments.groups.user_count 职位当前人数
      @apiSuccess (200) {String} departments.groups.master_name 负责人姓名
      @apiSuccess (200) {String} departments.id 部门ID
      @apiSuccess (200) {Number} departments.id 部门ID
      @apiSuccess (200) {String} departments.name 部门名称
      @apiSuccess (200) {String} departments.description 部门描述
      @apiSuccess (200) {String} departments.clazz 部门类型 root-公司 normal-普通
      
      @apiSuccess (403) {String} message 错误信息 用户没有部门浏览权限

      @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
       [
        {
            "clazz": "root",
            "description": "董事会",
            "groups": [
                {
                    "clazz": "master",
                    "description": "董事长",
                    "id": 17,
                    "master_name": null,
                    "name": "董事长",
                    "quota": 1,
                    "user_count": 0
                },
                {
                    "clazz": "master",
                    "description": "管理员",
                    "id": 18,
                    "master_name": "肖静远",
                    "name": "管理员",
                    "quota": 2,
                    "user_count": 1
                },
                {
                    "clazz": "master",
                    "description": "总经理",
                    "id": 19,
                    "master_name": null,
                    "name": "总经理",
                    "quota": 1,
                    "user_count": 0
                }
            ],
            "id": 9,
            "name": "董事会"
        },
        {
            "clazz": "normal",
            "description": "销售部",
            "groups": [
                {
                    "clazz": "master",
                    "description": "销售经理",
                    "id": 20,
                    "master_name": "祝菲",
                    "name": "销售主管",
                    "quota": 1,
                    "user_count": 1
                },
                {
                    "clazz": "normal",
                    "description": "销售员",
                    "id": 21,
                    "master_name": null,
                    "name": "销售员",
                    "quota": 1,
                    "user_count": 0
                },
                {
                    "clazz": "outer",
                    "description": "<p>1. 努力提高自身的知名度、信用度、美誉度，维护好自身光辉形象。 </p>\n<p>2. 利用自己的人脉资源,通过各种分享和传播渠道，帮助企业添加有效客户。</p>\n<p>3. 与客户保持良好沟通，提高企业在客户中的口碑。</p>",
                    "id": 54,
                    "master_name": null,
                    "name": "导购员",
                    "quota": 0,
                    "user_count": 0
                }
            ],
            "id": 10,
            "name": "营销部"
        },
        {
            "clazz": "normal",
            "description": "行政部",
            "groups": [
                {
                    "clazz": "master",
                    "description": "行政人事经理",
                    "id": 22,
                    "master_name": null,
                    "name": "人事主管",
                    "quota": 1,
                    "user_count": 0
                },
                {
                    "clazz": "normal",
                    "description": "",
                    "id": 44,
                    "master_name": null,
                    "name": "行政助理",
                    "quota": 1,
                    "user_count": 0
                }
            ],
            "id": 11,
            "name": "人事部"
        }
    ]
    """

    # Team_Construction - 部门列表
    def Team_Construction_departments_list_api(self, team_id, has_groups=None, ex=None):
        '''
        获取指定团队的指定职位详情。（该接口需要职位的浏览权限）
        :param team_id      :   团队ID
        :param has_groups   :   是否附加该部门的职位列表。（如提供该参数则该接口还需拥有职位的浏览权限）
        :param ex           :   为true时，则排除掉导购员职位
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'has_groups': has_groups,
            'ex': ex
        }

        # 2.替换id
        self.Team_Construction_departments_list = self.Team_Construction_departments_list.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_departments_list, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 部门列表', url=self.Team_Construction_departments_list, method='get')

        # 5.返回
        return response

    """
         @api {get} /api/v1/team/:team_id/departments/mine 部门列表（我的部门）
         @apiGroup Team Construction
         @apiName departments_mine
         @apiDescription 获取指定团队的当前用户所在的部门列表。（该接口需要部门及员工的浏览权限）用于查看我所在部门的相关信息

         @apiParam {String} token
         @apiParam {Number} team_id  团队ID
         @apiParam {String} [q] 按成员姓名模糊检索

         @apiParamExample {json} Request-Example:
         {
            'token': 'e4423f326ab0a7f7fc64c08689ee403d', 
            'team_id': '4835', 
            'q': None
         }

         @apiSuccess (200) {Object[]} departments 部门
         @apiSuccess (200) {Object[]} departments.users 部门员工
         @apiSuccess (200) {Number} departments.users.id 部门员工ID
         @apiSuccess (200) {String} departments.users.name 部门员工姓名
         @apiSuccess (200) {Object[]} departments.users.groups 员工职位
         @apiSuccess (200) {Number} departments.users.id 员工职位ID
         @apiSuccess (200) {Number} departments.users.name 职位名称
         @apiSuccess (200) {Number} departments.id 部门ID
         @apiSuccess (200) {String} departments.name 部门名称

         @apiSuccess (403) {String} message 错误信息 用户没有部门浏览权限

         @apiSuccessExample {json} Success-Response:
         HTTP/1.1 200 OK
          [
            {
                "id": 9,
                "name": "董事会",
                "users": [
                    {
                        "groups": [
                            {
                                "id": 18,
                                "name": "管理员"
                            }
                        ],
                        "id": 1654,
                        "mobile": "13027104206",
                        "name": "肖静远"
                    }
                ]
            }
          ]
       """

    # Team_Construction - 部门列表(我的部门)
    def Team_Construction_departments_mine_api(self, team_id, q=None):
        '''
        获取指定团队的指定职位详情。（该接口需要职位的浏览权限）
        :param team_id      :   团队ID
        :param q            :   按成员姓名模糊检索
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'team_id': team_id,
            'q': q
        }

        # 2.替换id
        self.Team_Construction_departments_mine = self.Team_Construction_departments_mine.replace(":team_id", team_id)

        # 3.发送请求
        response = self.R.get_function(self.Team_Construction_departments_mine, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 部门列表(我的部门)', url=self.Team_Construction_departments_mine, method='get')

        # 5.返回
        return response

    """
     @api {put} /api/v1/team/:team_id/departments/:id 部门更新(未使用)
     @apiGroup Team Construction
     @apiName update_department
     @apiDescription 更新指定团队的指定部门。（该接口需要部门的更新权限）

     @apiParam {String} token
     @apiParam {Number} team_id  团队ID
     @apiParam {Number} id  部门ID
     @apiParam {String} name  部门名称
     @apiParam {String} description 部门描述

     @apiParamExample {json} Request-Example:
     {
        'token': 'e4423f326ab0a7f7fc64c08689ee403d', 
        'team_id': '4835', 
        'id':'1234',
        'name':'人事部'
        'description':'description for this department'
     }

     @apiSuccess (200) {String} success 成功状态

     @apiSuccess (403) {String} message 错误信息 用户没有部门更新权限

     @apiSuccessExample {json} Success-Response:
     HTTP/1.1 200 OK
      {
        'success' : true
      }
   """

    # Team_Construction - 部门更新(未使用)
    def Team_Construction_departments_update_api(self, team_id, id, name, description):
        '''
        更新指定团队的指定部门。（该接口需要部门的更新权限）
        :param team_id      :   团队ID
        :param id           :   部门ID
        :param name         :   部门名称
        :param description  :   部门描述
        :return:
        '''
        # 1.组装token和data
        data = {
            'token': self.token,
            'id': id,
            'name':name,
            'description':description
        }

        # 2.替换id
        self.Team_Construction_departments_update = self.Team_Construction_departments_update.replace(":team_id", team_id)
        self.Team_Construction_departments_update = self.Team_Construction_departments_update.replace(":id", id)

        # 3.发送请求
        response = self.R.put_function(self.Team_Construction_departments_update, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Team_Construction - 部门列表(我的部门)', url=self.Team_Construction_departments_update, method='put')

        # 5.返回
        return response


team = TeamConstruction()
# Team_Construction - 业务列表
# team.Team_Construction_business_list_api(team_id='4835')

# Team_Construction - 业务开启
# team.Team_Construction_business_open_api(team_id='5710', id='10')

# Team_Construction - 员工主动退出
# team.Team_Construction_employee_quit_api(team_id='5712')

# Team_Construction - 员工任免
# team.Team_Construction_employee_assign_api(team_id='4835',id='5de2ab00-f4f4-4d4a-8641-076e58a6492e',group_ids='44')

# Team_Construction - 员工列表
# team.Team_Construction_employee_list_api(team_id='4835')

# Team_Construction - 员工新增-邀请
# team.Team_Construction_employee_add_api(team_id='4835',stranger_ids='183262')

# Team_Construction - 员工移除
# team.Team_Construction_employee_delete_api(team_id='4835', user_ids='d66dcb63-107f-4d30-a632-d97882b7465f')

# Team_Construction - 导购名额开关-切换
# team.Team_Construction_quota_switch_api(team_id='4835', event='off')

# Team_Construction - 是否是团队员工
# team.Team_Construction_is_joined_api(team_id='4835')

# Team_Construction - 机构成员列表
# team.Team_Construction_members_list_api(team_id='5029')

# Team_Construction - 模块权限
# team.Team_Construction_can_do_api(team_id='4835')

# Team_Construction - 职位列表
# team.Team_Construction_groups_list_api(team_id='4835', dept_id='9')

# Team_Construction - 职位更新
# team.Team_Construction_groups_update_api(team_id='4835', id='18', quota='2')

# Team_Construction - 职位申请-处理
# team.Team_Construction_groups_application_api(team_id='4835',ids='',event='reject')

# Team_Construction - 职位详情
# team.Team_Construction_groups_detail_api(team_id='4835', role_alias='outer_guide')

# Team_Construction - 部门列表
# team.Team_Construction_departments_list_api(team_id='4835', has_groups='true')

# Team_Construction - 部门列表(我的部门)
# team.Team_Construction_departments_mine_api(team_id='4835')
