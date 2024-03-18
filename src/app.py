"""屎山代码警告！！！！"""


from PySide6.QtWidgets import (QApplication, QMainWindow
                                 ,QFrame,QHBoxLayout, QPushButton,
                               QMessageBox,QGroupBox,QVBoxLayout, QWidget,QSizePolicy)
from  PySide6.QtCore import Qt,Slot,QObject,Signal
from  PySide6 import QtGui
from  PySide6.QtGui import QFont
from  src.views.searchVoiceView import searchVoicelView
from src.views.searchNovelView import searchNovelView
from  src.views.editWebSiteView import editWebSiteView
from src.views.settingView import  settingView
from src.views.webSiteManagerView import webSiteManagerView
from src.setting.settingManager import settingManager
from src.views.rulesManagerView import rulesManagerView
from src.views.editRuleView import editRuleView
import sys
import configparser
try:
    #读取配置
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read('config.ini',encoding='utf-8')

    STYLEPATH = config['CONFIGS']['STYLEPATH']
    SETTINGSPATH=config['CONFIGS']['SETTINGSPATH']
    RULESPATH = config['CONFIGS']['RULESPATH']
    DATAPATH = config['CONFIGS']['DATAPATH']
except:
    sys.exit()
class appWindow(QMainWindow,QObject):
    """主窗口"""

    #视图
    views={
        "search_novel":searchNovelView,
        "search_voice":searchVoicelView,
        "website_manage":webSiteManagerView,
        "edit_website":editWebSiteView,
        "setting":settingView,
        "rules_manager":rulesManagerView,
        "edit_rule":editRuleView,

    }

    #编辑网站信号
    editWebSiteSignal=Signal(str,str,str,str,str)
    # id name url type

    editRuleSignal=Signal(str)
    def __init__(self):
        """初始化"""
        super().__init__()
        #加载设置
        self.setting()
        #当前视图
        self.current_view="search_novel"
        #初始化ui
        self.initUI()
        #注册事件
        self.register_event()
    def initUI(self):
        #设置主题
        self.qss=self.getQss(self.theme)
        self.setStyleSheet(self.qss)
        #设置中心
        self.setCentralWidget(QWidget())
        self.centralWidget().setObjectName("centralWidget")
        #添加应用图标
        self.setWindowIcon(QtGui.QIcon('xyCNovel.png'))
        #设置窗口标题
        self.setWindowTitle('xyCNovel')
        #卡片布局
        self.rootLayout = QHBoxLayout(self.centralWidget())


        """左边"""
        self.leftWidget = QWidget()
        self.leftWidget.setObjectName("leftWidget")
        self.rootLayout.addWidget(self.leftWidget)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setAlignment(Qt.AlignTop)
        self.leftWidget.setLayout(self.leftLayout)
        self.leftWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        #self.leftWidget.setStyleSheet("background-color: red")

        """组"""
        #搜索
        self.leftSearchGroupBox = QGroupBox("搜索书籍")
        self.leftSearchGroupBox.setFont(self.font())
        self.leftLayout.addWidget(self.leftSearchGroupBox)
        self.leftSearchGroupLayout = QVBoxLayout()
        self.leftSearchGroupBox.setLayout(self.leftSearchGroupLayout)

        #阅读
        self.leftReadGroupBox = QGroupBox("阅读")
        self.leftReadGroupBox.setFont(self.font())
        self.leftLayout.addWidget(self.leftReadGroupBox)
        self.leftReadGroupLayout = QVBoxLayout()
        self.leftReadGroupBox.setLayout(self.leftReadGroupLayout)

        #下载
        self.leftDownloadGroupBox = QGroupBox("下载")
        self.leftDownloadGroupBox.setFont(self.font())
        self.leftLayout.addWidget(self.leftDownloadGroupBox)
        self.leftDownloadGroupLayout = QVBoxLayout()
        self.leftDownloadGroupBox.setLayout(self.leftDownloadGroupLayout)

        #网站
        self.leftWebsiteGroupBox = QGroupBox("网站")
        self.leftWebsiteGroupBox.setFont(self.font())
        self.leftLayout.addWidget(self.leftWebsiteGroupBox)
        self.leftWebsiteGroupLayout = QVBoxLayout()
        self.leftWebsiteGroupBox.setLayout(self.leftWebsiteGroupLayout)

        #设置
        self.leftSettingGroupBox = QGroupBox("设置")
        self.leftSettingGroupBox.setFont(self.font())
        self.leftLayout.addWidget(self.leftSettingGroupBox)
        self.leftSettingGroupLayout = QVBoxLayout()
        self.leftSettingGroupBox.setLayout(self.leftSettingGroupLayout)



        """按钮"""
        #搜索书籍
        self.search_novel_button=QPushButton("搜索书籍")
        self.search_novel_button.setFont(self.font())
        self.search_novel_button.setFixedSize(200, 30)
        self.leftSearchGroupLayout.addWidget(self.search_novel_button)

        #有声小说搜索
        self.search_voice_button=QPushButton('搜索有声小说')
        self.search_voice_button.setFont(self.font())
        self.search_voice_button.setFixedSize(200, 30)
        self.leftSearchGroupLayout.addWidget(self.search_voice_button)

        #小说书架
        self.novel_shelf_button=QPushButton("小说书架")
        self.novel_shelf_button.setFont(self.font())
        self.novel_shelf_button.setFixedSize(200, 30)
        self.leftReadGroupLayout.addWidget(self.novel_shelf_button)

        #有声书架
        self.voice_shelf_button=QPushButton("有声书架")
        self.voice_shelf_button.setFont(self.font())
        self.voice_shelf_button.setFixedSize(200, 30)
        self.leftReadGroupLayout.addWidget(self.voice_shelf_button)

        #下载小说
        self.download_novel_button=QPushButton("下载小说")
        self.download_novel_button.setFont(self.font())
        self.download_novel_button.setFixedSize(200, 30)
        self.leftDownloadGroupLayout.addWidget(self.download_novel_button)

        #下载有声小说
        self.download_voice_button=QPushButton("下载有声小说")
        self.download_voice_button.setFont(self.font())
        self.download_voice_button.setFixedSize(200, 30)
        self.leftDownloadGroupLayout.addWidget(self.download_voice_button)

        #下载记录
        self.download_record_button=QPushButton("下载记录")
        self.download_record_button.setFont(self.font())
        self.download_record_button.setFixedSize(200, 30)
        self.leftDownloadGroupLayout.addWidget(self.download_record_button)



        #网站管理
        self.website_manage_button=QPushButton("网站管理")
        self.website_manage_button.setFont(self.font())
        self.website_manage_button.setFixedSize(200, 30)
        self.leftWebsiteGroupLayout.addWidget(self.website_manage_button)
        #规则管理
        self.rule_manage_button=QPushButton("规则管理")
        self.rule_manage_button.setFont(self.font())
        self.rule_manage_button.setFixedSize(200, 30)
        self.leftWebsiteGroupLayout.addWidget(self.rule_manage_button)


        #设置
        self.setting_button=QPushButton("设置")
        self.setting_button.setFont(self.font())
        self.setting_button.setFixedSize(200, 30)
        self.leftSettingGroupLayout.addWidget(self.setting_button)

        """右边"""
        self.rightWidget = self.views[self.current_view](self)
        self.rootLayout.addWidget(self.rightWidget)
        #充满父容器
        self.rightWidget.setSizePolicy(QSizePolicy.Expanding,  QSizePolicy.Expanding)
    @Slot(str,str,str,str)
    def edit_website(self,id,name,url,type,rule):
        """编辑网站"""
        self.swv("edit_website")
        self.editWebSiteSignal.emit(id,name,url,type,rule)
    def register_slot(self,viewname):
        """注册槽"""
        if viewname=="website_manage":
            self.rightWidget.addWebSiteSignal.connect(self.switch_view("edit_website"))
            self.rightWidget.editWebSiteSignal.connect(self.edit_website)
        elif  viewname=="setting":
            self.rightWidget.settingChanged.connect(self.setting_changed)
        elif   viewname=="edit_website":
            self.rightWidget.savaFinish.connect(self.switch_view("website_manage"))
        elif    viewname=="rules_manager":
            self.rightWidget.addRuleSignal.connect(self.switch_view("edit_rule"))
            self.rightWidget.editRuleSignal.connect(self.edit_rule)
        elif      viewname=="edit_rule":
            self.rightWidget.savaFinish.connect(self.switch_view("rules_manager"))

    @Slot(str)

    def edit_rule(self,name):
        self.swv("edit_rule")
        self.editRuleSignal.emit(name)
    @Slot()
    def setting_changed(self):
        """设置改变槽"""
        self.setting()
        self.initUI()
        self.register_event()
        self.rightWidget.hide()
        self.swv("setting")


    def swv(self,view_name):
        """切换view"""
        self.rightWidget.hide()

        self.rightWidget = self.views[view_name](self)
        self.rootLayout.addWidget(self.rightWidget)
        self.rightWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.register_slot(view_name)
        self.current_view = view_name


    #事件注册
    def  register_event(self):
        """注册事件"""
        self.search_novel_button.clicked.connect(self.switch_view("search_novel"))
        self.search_voice_button.clicked.connect(self.switch_view("search_voice"))
        self.novel_shelf_button.clicked.connect(self.switch_view("novel_shelf"))
        self.voice_shelf_button.clicked.connect(self.switch_view("voice_shelf"))
        self.download_voice_button.clicked.connect(self.switch_view("download_voice"))
        self.download_record_button.clicked.connect(self.switch_view("download_record"))
        self.website_manage_button.clicked.connect(self.switch_view("website_manage"))
        self.setting_button.clicked.connect(self.switch_view("setting"))
        self.download_novel_button.clicked.connect(self.switch_view("download_novel"))
        self.rule_manage_button.clicked.connect(self.switch_view("rules_manager"))


    @Slot()
    #视图切换
    def switch_view(self, view_name):
        """切换view"""
        """生成一个绑定指定view的切换函数"""
        def switch(event=None):
            #判断是否在当前view
            if self.current_view != view_name:
                #判断view是否存在
                if view_name in self.views.keys():
                    self.swv(view_name)
        #返回切换到指定view的函数
        return  switch

    def getQss(self,theme):
        try:
            qss=open(STYLEPATH+"style"+"_"+theme+".qss", "r").read()
            return qss
        except:
            QMessageBox.warning(self, "警告", "找不到样式文件")
            sys.exit()
    def setting(self):
        self.theme=settingManager.get_ui_theme_name(SETTINGSPATH)
        self.setFont(QFont(settingManager.get_ui_font_name(SETTINGSPATH)))

if __name__ == '__main__':
    app = QApplication([])
    window = appWindow()
    window.show()
    app.exec()


