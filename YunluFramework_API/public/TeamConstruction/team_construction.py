# Author:# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.public.TeamConstruction import *


# 空间
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

team = TeamConstruction()
team.Team_Construction_business_list_api(team_id='4835')
