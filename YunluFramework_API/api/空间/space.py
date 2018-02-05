# Author:Xiaojingyuan
__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework_API.api.空间 import *


# 空间
@ddt.ddt
class Space(Login):
    def __init__(self):
        Handle.__init__(self)
        # 1.接口路由
        # Space - 企业空间关闭
        self.url_closespace = self.cf.getURL('space', "url_closespace")

        # Space - 企业空间创建
        self.Space_org_create = self.cf.getURL('space', "Space_org_create")

        # Space - 图片标签列表
        self.Space_list = self.cf.getURL('space', 'Spaces_list')

        # Space - 图片标签删除
        self.Space_img_label_delete_id = self.cf.getURL('space', 'Space_img_label_delete_id')

        # Space - 图片标签新增
        self.Space_img_label_add = self.cf.getURL('space', 'Space_img_label_add')

        # Space - 文件夹中上传图片（个人）
        self.Space_folder_img_upload_id = self.cf.getURL('space', 'Space_folder_img_upload_id')

        # Space - 文件夹中列举图片（个人）
        self.Space_folder_list_img = self.cf.getURL('space', 'Space_folder_list_img')

        # Space - 文件夹公开设置
        self.Space_folder_open_setting = self.cf.getURL('space', 'Space_folder_open_setting')

        # Space - 文件夹列表
        self.Space_folder_list = self.cf.getURL('space', 'Space_folder_list')

        # Space - 文件夹列表(联系人所有）
        self.Space_folder_list_id = self.cf.getURL('space', 'Space_folder_list_id')

        # Space - 文件夹创建
        self.Space_folder_create = self.cf.getURL('space', 'Space_folder_create')

        # Space - 文件夹删除
        self.Space_folder_delete_id = self.cf.getURL('space', 'Space_folder_delete_id')

        # Space - 文件夹更新
        self.Space_folder_update_id = self.cf.getURL('space', 'Space_folder_update_id')

        # Space - 文件夹浏览记录
        self.Space_folder_browse = self.cf.getURL('space', 'Space_folder_browse')

        # Space - 热门空间名
        self.Space_popular_name = self.cf.getURL('space', 'Space_popular_name')

        # Space - 特定图片标签列表
        self.Space_img_label_list = self.cf.getURL('space', 'Space_specificimg_label_list')

        # Space - 特定图片标签删除
        self.Space_img_label_delete_id = self.cf.getURL('space', 'Space_specificimg_label_delete_id')

        # Space - 特定图片标签更新
        self.Space_img_label_update = self.cf.getURL('space', 'Space_specificimg_label_update')

        # Space - 空间中删除联系人(删除客户)
        self.Space_delete_contact_id = self.cf.getURL('space', 'Space_delete_contact_id')

        # Space - 空间中添加联系人(新增客户)
        self.Space_add_contac_id = self.cf.getURL('space', 'Space_add_contac_id')

        # Space - 空间公开设置
        self.Space_switch_setting = self.cf.getURL('space', 'Space_switch_setting')

        # Space - 空间列表
        self.Spaces_list = self.cf.getURL('space', 'Spaces_list')

        # Space - 空间创建
        self.Space_private_create = self.cf.getURL('space', 'Space_private_create')

        # Space - 空间删除
        self.Space_private_delete_id = self.cf.getURL('space', 'Space_private_delete_id')

        # Space - 空间升级
        self.Space_upgrade = self.cf.getURL('space', 'Space_upgrade')

        # Space - 空间更新
        self.Space_update_id = self.cf.getURL('space', 'Space_update_id')

        # Space - 空间概况
        self.Space_overview_id = self.cf.getURL('space', 'Space_overview_id')

        # Space - 空间类型列表
        self.Space_type_list = self.cf.getURL('space', 'Space_type_list')

        # Space - 空间联系人列表(非当前用户)
        self.Space_contact_list_id = self.cf.getURL('space', 'Space_contact_list_id')

        # 2.token
        self.token = self.get_token()

        # 3. 创建请求对象
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

    """
    @api {get} /api/v1/galleries 私人空间-文件夹列表
    @apiGroup Space
    @apiName galleries
    @apiDescription 用于获取私人空间下面的文件夹列表，可以传联系人ID，用户ID，私人空间ID

    @apiParam {String} token 
    @apiParam {Number} [stranger_id]  联系人ID：提供此ID则获取该联系人下的文件夹，人脉中可用
    @apiParam {String} [user_id] 用户UUID：提供此ID则获取该用户下的文件夹，人脉中可用
    @apiParam {Number} [cluster_id] 私人空间ID：提供此ID则获取该空间下的文件夹，一般在进入私人空间中调用
    
    @apiParamExample {json} Request-Example:
    {
      'token': 'e156d8f635eaa66230368130ed207579', 
      'stranger_id': None,
      'user_id': None,
      'cluster_id': '8339'
    }

    
    @apiSuccess {Object[]} gallery 返回文件夹对象，json数据
    @apiSuccess {Number}  id 文件夹ID
    @apiSuccess {String} name  文件夹名称
    @apiSuccess {Number} cluster_id  空间ID
    @apiSuccess {Number} count  文件夹图片数量
    @apiSuccess {Number} last_photo  文件夹最新图片
    @apiSuccess {String="on","off"}  disclosure 是否公开 
    
    @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
      {
        "gallery": [
            {
                "can_click": false,
                "clazz": "user_custom",
                "cluster_class_id": 68,
                "cluster_id": 8339,
                "count": 0,
                "disclosure": "off",
                "id": 19828,
                "last_photo": "",
                "name": "测试文件夹api",
                "photos": []
                }
            ]
        }
    
    """

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

    """
           @api {post} /api/v1/galleries 私人空间-文件夹创建
           @apiGroup Space
           @apiName create_gallery
           @apiDescription 创建文件夹到私人空间

           @apiParam {String} token
           @apiParam {Number} cluster_id 私人空间ID
           @apiParam {String} name 文件夹名称

           @apiParamExample {json} Request-Example:
           {
            'token': 'e156d8f635eaa66230368130ed207579', 
            'cluster_id': '8341', 
            'name': 'api测试文件夹'
           }

           @apiSuccess (201) {String} success 成功状态
           @apiSuccess (201) {Number} id 文件夹创建成功后id 

           @apiSuccessExample {json} Success-Response:
            HTTP/1.1 201 OK
            {
                "id": 19831,
                "success": true
            }

        """

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
        self.plog.printlog(data, response, describle='Space - 文件夹创建', url=self.Space_folder_create, method='post')

        # 4.返回
        return response

    """
          @api {delete} /api/v1/galleries/:id 私人空间-文件夹删除
          @apiGroup Space
          @apiName delete_gallery
          @apiDescription 私人空间删除当前用户文件夹
    
          @apiParam {String} token
          @apiParam {Number} id 文件夹ID
    
          @apiParamExample {json} Request-Example:
          {
           'token': 'e156d8f635eaa66230368130ed207579', 
           'id': '19833',
          }
    
          @apiSuccess  {String} success 成功状态
    
          @apiSuccessExample {json} Success-Response:
           HTTP/1.1 200 OK
           {
               "success": true
           }

    """

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

    """
       @api {put} /api/v1/galleries 私人空间-文件夹更新
       @apiGroup Space
       @apiName update_gallery
       @apiDescription 私人空间更新文件夹(如：更新文件夹名称)

       @apiParam {String} token
       @apiParam {Number} id 文件夹ID
       @apiParam {Number} [cluster_id] 私人空间ID
       @apiParam {String} [name] 文件夹名称

       @apiParamExample {json} Request-Example:
       {
        'token': 'e156d8f635eaa66230368130ed207579', 
        'id': '19833',
        'cluster_id': '8342', 
        'name': '测试文件夹api'
       }

       @apiSuccess  {String} success 成功状态

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "success": true
        }

    """

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
            'id': id,
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

    """
       @api {get} /api/v1/spaces/names 热门空间名
       @apiGroup Space
       @apiName names
       @apiDescription 用于获取常用的空间名，用于创建空间时的空间名推荐

       @apiParam {String} count  空间名数量，默认10个
       @apiParam {Number} [class_id] 空间类型，来源：根据"私人空间类型列表"接口获取空间类型

       @apiParamExample {json} Request-Example:
       {
        'token': 'e156d8f635eaa66230368130ed207579', 
        'class_id': 67, 
        'count': None
        }



       @apiSuccess {String} success 成功状态
       @apiSuccess {String}  names 热门空间名 

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
        "names": [
            "舌尖上的中国",
            "美食",
            "民以食为天",
            "茶",
            "厨艺秀",
            "正宗东海海鲜《海鲜大礼》",
            "吃货世界",
            "吃货的世界",
            "我的衣柜",
            "我的店铺"
        ],
        "success": true
        }

       """

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

    """
       @api {post} /api/v1/spaces 空间列表
       @apiGroup Space
       @apiName spaces
       @apiDescription 获取指定用户的空间列表
    
       @apiParam {String} token
       @apiParam {String} [q] 根据空间名过滤
       @apiParam {String="private", "organization", "representative", "master", "normal", "outer"} class private-获取所有私人空间；
                                                                                                    organization-获取所有企业空间（包括自创的与加盟的）；未提供该值则返回所有空间；
                                                                                                    representative-获取当前用户是其机构法人的企业空间；
                                                                                                    master-获取当前用户是其高管的企业空间；
                                                                                                    normal-获取当前用户是其助理级员工的企业空间；
                                                                                                    outer-获取当前用户是其导购员的企业空间
       @apiParam {String} [stranger_id] 联系人ID，提供该值时返回的结果中包含字段opened(空间是否已对指定联系人开放，提供参数 stranger_id 时，包含该字段)

        
       @apiParamExample {json} Request-Example:
       {
           'token': 'e156d8f635eaa66230368130ed207579', 
           'q': 'api测试', 
           'class': None
       }
        
        
       @apiSuccess  {Object[]} space 空间对象
       @apiSuccess  {String} name 空间名称 
       @apiSuccess  {Number} cluster_id 私人空间ID
       @apiSuccess  {Number} organization_id 机构空间ID
       @apiSuccess  {Number} service_id 服务类型ID
       @apiSuccess  {String} logo_url 机构空间-LOGO URL
       @apiSuccess  {Number} class_id 空间类型ID(案例中为私人空间类型ID)
       @apiSuccess  {String} owner_class 空间所有类型 private - 私有空间; master - 堂主空间; member - 加盟空间
       @apiSuccess  {Number} locked 空间是否已暂时关闭
       @apiSuccess  {Number} gallery_count 空间所属的目录数
       @apiSuccess  {Boolean} opened 空间是否已对指定联系人开放，提供参数 stranger_id 时，包含该字段
       @apiSuccess  {Boolean} organization_state 机构状态，企业空间时，包含该字段

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 201 OK
        [
            {
                "aliaz": null,
                "class_id": 67,
                "cluster_id": 8339,
                "company": null,
                "disclosure": "off",
                "gallery_count": 0,
                "locked": false,
                "logo_url": null,
                "name": "api测试",
                "organization_id": null,
                "owner_class": "private",
                "service_id": null,
                "vocation": null
            }
        ]

    """

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

    """
       @api {post} /api/v1/clusters 私人空间创建
       @apiGroup Space
       @apiName cluster
       @apiDescription 当前用户用于创建私人空间

       @apiParam {String} token
       @apiParam {String} name 私人空间名称
       @apiParam {Number} [class_id] 空间类型，来源：根据"私人空间类型列表"接口获取空间类型

       @apiParamExample {json} Request-Example:
       {
           'token': 'e156d8f635eaa66230368130ed207579', 
           'name': 'api测试', 
           'class_id': 67
       }

       @apiSuccess (201) {String} success 成功状态
       @apiSuccess (201) {Number} id 空间ID 

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 201 OK
        {
            "id": 8339,
            "success": true
        }
    
    """

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

    """
      @api {delete} /api/v1/clusters/:id 私人空间删除
      @apiGroup Space
      @apiName delete_cluster
      @apiDescription 删除当前用户的私人空间

      @apiParam {String} token
      @apiParam {Number} id 空间ID

      @apiParamExample {json} Request-Example:
      {
       'token': 'e156d8f635eaa66230368130ed207579', 
       'id': '19833',
      }

      @apiSuccess  {String} success 成功状态

      @apiSuccessExample {json} Success-Response:
       HTTP/1.1 200 OK
       {
           "success": true
       }

    """
    # Space - 空间删除（私人空间）
    def Space_private_delete_id_api(self, id):
        '''
        删除当前用户的私人空间
        :param id : 空间id
        :return:
        '''

        # 1.组装数据
        data = {
            "token": self.token,
            "id": id
        }

        # 2.替换id
        url = self.Space_private_delete_id.replace(':id', id)

        # 3. 发送请求
        response = self.R.delete_function(url, data)

        # 4.打印日志
        self.plog.printlog(data, response, describle='Space - 私人空间删除', url=url, method='delete')

        # 5.返回
        return response

    """
          @api {put} /api/v1/clusters/8341 私人空间更新
          @apiGroup Space
          @apiName 
          @apiDescription 当前用户更新私人空间，例如更新私人空间名称、空间类型

          @apiParam {String} token
          @apiParam {Number} id 空间ID
          @apiParam {String} [name] 私人空间名称
          @apiParam {Number} [class_id] 空间类型ID

          @apiParamExample {json} Request-Example:
          {
            'token': 'e156d8f635eaa66230368130ed207579', 
            'id': '8341', 
            'name': '测试api', 
            'class_id': '68'
          }

          @apiSuccess {String} success 成功状态

          @apiSuccessExample {json} Success-Response:
           HTTP/1.1 200 OK
           {
               "success": true
           }

       """

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

    """
       @api {get} /api/v1/clusters/:id 私人空间-空间概况
       @apiGroup Space
       @apiName show_cluster
       @apiDescription 私人空间概况

       @apiParam {String} token
       @apiParam {Number} id 私人空间ID

       @apiParamExample {json} Request-Example:
       {
        'token': 'e156d8f635eaa66230368130ed207579', 
        'id': '8343',
       }

       @apiSuccess  {Number} id 私人空间ID
       @apiSuccess {String} name 私人空间名称
       @apiSuccess {Number} class_id 空间类型ID
       @apiSuccess {String} class_name 空间类型名称
       @apiSuccess {Number} galleries_count 空间中的文件夹个数
       @apiSuccess {Number} clients_count 空间中的客户数量

       @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "class_id": 68,
            "class_name": "居住",
            "clients_count": 0,
            "galleries_count": 1,
            "id": 8343,
            "name": "测试api"
        }

    """

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

    """
        @api {get} /api/v1/space_classes 私人空间类型列表
        @apiGroup Space
        @apiName classes
        @apiDescription 获取私人空间下面的可选类型列表

        @apiParam {Number} [parent_id] 空间类型ID，提供该值则返回为目录类型

        @apiParamExample {json} Request-Example:
        {
            'token': 'e156d8f635eaa66230368130ed207579', 
            'parent_id': None
        }


        @apiSuccess {Object[]} space_class 返回空间类型对象，json数据
        @apiSuccess {String}  id 类型ID
        @apiSuccess {String} name  类型名称
        @apiSuccess {String} aliaz  类别别名

        @apiSuccessExample {json} Success-Response:
          HTTP/1.1 200 OK
          [
            {
                "aliaz": "food",
                "id": 67,
                "name": "食物"
            },
            {
                "aliaz": "house",
                "id": 68,
                "name": "居住"
            },
            {
                "aliaz": "traffic",
                "id": 69,
                "name": "出行"
            },
            {
                "aliaz": "education",
                "id": 70,
                "name": "学习"
            },
            {
                "aliaz": "health",
                "id": 71,
                "name": "健康"
            },
            {
                "aliaz": "intercourse",
                "id": 72,
                "name": "社交"
            },
            {
                "aliaz": "vocation",
                "id": 73,
                "name": "工作"
            },
            {
                "aliaz": "art",
                "id": 74,
                "name": "文艺"
            },
            {
                "aliaz": "amusement",
                "id": 75,
                "name": "娱乐"
            },
            {
                "aliaz": "beauty",
                "id": 76,
                "name": "美护"
            },
            {
                "aliaz": "other",
                "id": 77,
                "name": "其他"
            },
            {
                "aliaz": "clothing",
                "id": 66,
                "name": "穿衣"
            }
        ]


        """

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
sp = Space()

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
