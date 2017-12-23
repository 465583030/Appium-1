__author__ = 'Administrator'
# -*- coding: utf-8 -*-
from YunluFramework.testcase.空间.私人空间.test1_1创建私人空间 import *


# 创建私人空间
@ddt.ddt
class perspace_CreateP(unittest.TestCase):
    # 1.创建数据库操作对象
    d = DataMysql()
    sql00 = "select * from test1_1_percreatespace_00"
    sql02 = "select * from test1_1_percreatespace_02"
    data00 = d.select(sql00, 0)
    data02 = d.select(sql02, 0)

    # # 1.全局测试数据
    # d = DataInfo("space.xls")  # 创建DataInfo()对象
    # spacename_1 = d.cell("test006-私人空间", 2, 13)  # 空间名:appium私人空间
    # # 2.各空间类型下热门空间名第1个标签
    # clothesT_1 = (d.cell("test006-私人空间", 3, 1))  # 我的衣柜0
    # foodT_1 = (d.cell("test006-私人空间", 3, 2))  # 舌尖上的中国1
    # liveT_1 = (d.cell("test006-私人空间", 3, 3))  # 我爱我家2
    # walkT_1 = (d.cell("test006-私人空间", 3, 4))  # 旅游照片3
    # studyT_1 = (d.cell("test006-私人空间", 3, 5))  # 互联网十4
    # healthT_1 = (d.cell("test006-私人空间", 3, 6))  # 强身健体5
    # socialT_1 = (d.cell("test006-私人空间", 3, 7))  # 同学们6
    # workT_1 = (d.cell("test006-私人空间", 3, 8))  # 办公场所7
    # literatureT_1 = (d.cell("test006-私人空间", 3, 9))  # 文娱空间8
    # entertainmentT_1 = (d.cell("test006-私人空间", 3, 10))  # 电影放映室9
    # beautyT_1 = (d.cell("test006-私人空间", 3, 11))  # Onlyyou10
    # otherT_1 = (d.cell("test006-私人空间", 3, 12))  # 摄影11

    # 2.初始化
    @classmethod
    def setUpClass(self):
        # 1.建立连接信息
        cnn = Connect()
        self.driver = cnn.connect()
        # 2.创建工具类
        self.tools = Tools(self.driver)  # tools工具
        # 3.创建_CreatePersonalSpaceHandle公有定位控件对象
        self.handle = SPACEHANDLE5(self.driver)
        # 4.创建读取配置信息对象
        cf = GlobalParam('config', 'path_file.conf')
        # 5. 获取截图路径、日志路径、日志名
        self.screen_path = cf.getParam('space', "per_path_001_1")  # 通过配置文件获取截图的路径
        self.logfile = cf.getParam('log', "logfile")  # 日志文件名
        # 6.创建日志记录模块
        self.log = Log(self.logfile)
        # 7.创建空间公有操作对象
        self.common = CommonSpace(self.handle, self.log, self.tools)
        sleep(1)
        # 8.打印日志
        self.log.info('****************************************用例开始！****************************************')
        self.log.info("------------START:test1_1创建私人空间CreatePersonSpace001_1.py------------")

    # 3.释放资源
    def tearDownClass(self):
        # 1.打印日志
        self.log.info("------------END:test1_1创建私人空间CreatePersonSpace001_1.py------------")
        self.log.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~用例结束！~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # 2.关闭driver
        # self.driver.quit()

    # 4.测试用例
    # 4.1判断空间是否已存在
    @ddt.data(data00)
    @ddt.unpack
    def test_percreateSpace00(self, spacename):
        '''判断私人空间是否重复
        :param spacename: 空间名
        :return:
        '''
        try:
            self.common.enter_space(spacename)  # 查找空间
            self.common.click_org_menu('close')  # 点击关闭
            self.handle.Kjlb_browseorgspace_menu_close_confirm_click()  # 确认关闭
            self.log.info('点击确认关闭')
        except:
            pass

    # 4.1进入空间
    def test_percreatesSapce01(self):
        '''进入空间首页
        :return:
        '''
        try:
            sleep(1)
            # 1.空间首页
            self.handle.Kjlb_click()
            self.log.info('点击进入空间首页')
            # 2.点击+按钮
            self.handle.Kjlb_mainmenu_click()
            self.log.info('点击：+按钮')
            # 3.+私人空间
            self.handle.Kjlb_mainmenu_newpersonspace_click()
            self.log.info('点击+私人空间')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_percreatesSapce01 : %s" % err)
            raise err

    # 4.2 检查空间类型和标签对应关系
    @ddt.data(data02)
    @ddt.unpack
    def test_percreatesSpace02(self, clothesT, foodT, liveT, walkT, studyT,
                               healthT, socialT, workT, literatureT, entertainmentT,
                               beautyT, otherT):
        '''检查空间类型和标签对应关系
        :param clothesT: 衣
        :param foodT: 食
        :param liveT: 住
        :param walkT: 行
        :param studyT: 学习
        :param healthT: 健康
        :param socialT: 社交
        :param workT: 工作
        :param literatureT: 文艺
        :param entertainmentT: 娱乐
        :param beautyT: 美护
        :param otherT: 其它
        :return:
        '''
        try:
            # 4.选择空间类型-检查类型和推荐名对应
            AllLabel = []  # 把各标签下的推荐列表，存到AllLabel列表里面
            for a in range(12):  # 循环12次
                self.handle.Kjlb_mainmenu_newpersonspace_choosespacetype_click(a)  # 选择列表中第a个标签
                self.log.info('选择列表中的第{0}个标签'.format(a + 1))
                # sleep(1)
                # 把该标签下的推荐空间名存到一个列表中
                EveryLabel = []
                for i in self.handle.Kjlb_mainmenu_newpersonspace_suggestspacenametag_get():
                    text = i.text
                    EveryLabel.append(text)
                AllLabel.append(EveryLabel)
                self.handle.Kjlb_mainmenu_newpersonspace_changespacetype_click()  # 切换类型
            # print("AllLabel",AllLabel)
            # 4.1衣
            self.log.info("判断'衣'下的推荐标签")
            assert clothesT in AllLabel[0], "Clothes : The recommended name does not conform to type"
            # 4.2食
            self.log.info("判断'食'下的推荐标签")
            assert foodT in AllLabel[1], "Food : The recommended name does not conform to type"
            # 4.3住
            self.log.info("判断'住'下的推荐标签")
            assert liveT in AllLabel[2], "Live : The recommended name does not conform to type"
            # 4.4行
            self.log.info("判断'行'下的推荐标签")
            assert walkT in AllLabel[3], "Walk : The recommended name does not conform to type"
            # 4.5学习
            self.log.info("判断'学习'下的推荐标签")
            assert studyT in AllLabel[4], "StudyT : The recommended name does not conform to type"
            # 4.6健康
            self.log.info("判断'健康'下的推荐标签")
            assert healthT in AllLabel[5], "HealthT : The recommended name does not conform to type"
            # 4.7社交
            self.log.info("判断'社交'下的推荐标签")
            assert socialT in AllLabel[6], "Social : The recommended name does not conform to type"
            # 4.8工作
            self.log.info("判断'工作'下的推荐标签")
            assert workT in AllLabel[7], "Work : The recommended name does not conform to type"
            # 4.9文艺
            self.log.info("判断'文艺'下的推荐标签")
            assert literatureT in AllLabel[8], "LiteratureT : The recommended name does not conform to type"
            # 4.10娱乐
            self.log.info("判断'娱乐'下的推荐标签")
            assert entertainmentT in AllLabel[9], "Entertainment : The recommended name does not conform to type"
            # 4.11美护
            self.log.info("判断'美护'下的推荐标签")
            assert beautyT in AllLabel[10], "Beauty : The recommended name does not conform to type"
            # 4.12其它
            self.log.info("判断'其它'下的推荐标签")
            assert otherT in AllLabel[11], "Other : The recommended name does not conform to type"
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_percreatesSpace02 : %s" % err)
            raise err

    # 创建私人空间
    @ddt.data(data00)
    @ddt.unpack
    def test_percreateSpace03(self, spacename):
        '''创建私人空间
        :param spacename: 空间名
        :return:
        '''
        try:
            # 5.输入空间名称、文件夹名-保存
            self.handle.Kjlb_mainmenu_newpersonspace_choosespacetype_click(0)  # 选择衣服类型空间
            self.log.info('选择衣服类型空间')
            self.handle.Kjlb_mainmenu_newpersonspace_spacename_sendkeys(spacename)  # appium私人空间
            self.log.info('创建{0}空间'.format(spacename))
            self.handle.Kjlb_mainmenu_newpersonspace_save_click()  # 保存
            self.log.info('点击保存')
            # 6.返回到空间列表
            self.handle.Kjlb_mainmenu_newpersonspace_mainback_click()
            self.log.info('点击保存')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_percreateSpace03 : %s" % err)
            raise err

    # 关闭空间
    @ddt.data(data00)
    @ddt.unpack
    def test_percreateSpace04(self, spacename):
        '''关闭空间
        :param spacename:空间名
        :return:
        '''
        try:
            # 1.点击该空间
            self.common.enter_space(spacename)
            # 2.菜单栏
            self.handle.Kjlb_browseperspace_menu_click()
            self.log.info('点击菜单栏')
            # 3.编辑
            self.handle.Kjlb_browseperspace_menu_edit_click()
            self.log.info('点击编辑')
            # 4.删除空间
            self.handle.Kjlb_browseperspace_menu_edit_deletespace_click()
            self.log.info('点击删除空间')
            self.handle.Kjlb_browseperspace_menu_edit_deletespace_OK_click()
            self.log.info('点击确定删除')
        except Exception as err:
            self.tools.getScreenShot(self.screen_path, "ExceptionShot")
            self.log.error("test_percreateSpace04 : %s" % err)
            raise err
