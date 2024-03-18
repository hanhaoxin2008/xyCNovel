from PySide6.QtWidgets import QMessageBox,QAbstractItemView,QMenu,QHeaderView,QTableWidget,QTableWidgetItem,QHBoxLayout,QLabel,QWidget,QSizePolicy,QPushButton,QVBoxLayout
from  PySide6.QtCore import Qt,Signal,QObject
from PySide6.QtGui import QCursor,QAction
from src.webSiteManager.webSiteManager import webSiteManager
import configparser

#读取配置
config = configparser.ConfigParser()
config.optionxform = str
config.read('config.ini',encoding='utf-8')
DATAPATH = config["CONFIGS"]["DATAPATH"]

class webSiteManagerView(QWidget,QObject):
    addWebSiteSignal = Signal()
    editWebSiteSignal = Signal(str,str,str,str,str)
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.initUI()
        self.register_event()
        self.conn=webSiteManager.init(DATAPATH)
        self.load_data()
    def initUI(self):
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.rootLayout)

        self.toplayout=QHBoxLayout()
        self.rootLayout.addLayout(self.toplayout)
        self.toplayout.setAlignment(Qt.AlignLeft)

        self.title=QLabel('网站管理')
        #设置字体
        self.title.setFont(self.parent().font())
        #设置字体大小
        self.title.setStyleSheet('font-size:20px')
        self.title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.toplayout.addWidget(self.title)


        self.add_website_button=QPushButton('添加网站')
        self.add_website_button.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.add_website_button.setObjectName('add_website_button')
        self.add_website_button.setFixedSize(100,30)
        self.toplayout.addWidget(self.add_website_button)

        #网站列表
        self.website_list=QTableWidget()
        self.website_list.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.website_list.setFont(self.parent().font())
        self.website_list.setStyleSheet('font-size:15px')
        self.website_list.setObjectName('website_list')
        self.rootLayout.addWidget(self.website_list)
        #表头
        self.website_list.setColumnCount(5)
        self.website_list.setHorizontalHeaderLabels(['id','名称','网址','类型',"规则"])
        #设置列可拉伸
        self.website_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #隐藏左边序号
        self.website_list.verticalHeader().setVisible(False)
        #设置不可编辑
        self.website_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #自定义表项右键菜单
        self.website_list.setContextMenuPolicy(Qt.CustomContextMenu)
        #设置一次只能选中一行
        self.website_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.website_list.customContextMenuRequested.connect(self.show_menu)
        self.website_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.website_list.setAlternatingRowColors(True)
        self.website_list.setSortingEnabled(False)
        self.website_list.sortByColumn(0,Qt.AscendingOrder)
    def remove(self):
        """删除"""
        #确认删除
        reply = QMessageBox.question(self,'删除','是否删除',QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.No:
            return
        #获取选中行选中行
        row = self.website_list.currentIndex().row()
        #获取id
        id = self.website_list.item(row,0).text()
        #删除界面中对应行
        self.website_list.removeRow(row)
        #删除数据库中对应行
        webSiteManager.delete(conn=self.conn,id=id)
    def  modify(self):
        """修改"""
        #获取选中行
        row = self.website_list.currentIndex().row()
        #获取id,name,url,type
        id = self.website_list.item(row,0).text()
        name = self.website_list.item(row,1).text()
        url = self.website_list.item(row,2).text()
        type=self.website_list.item(row,3).text()
        rule=self.website_list.item(row,4).text()
        #发送信号
        self.editWebSiteSignal.emit(id,name,url,type,rule)
    def show_menu(self,event):
        """右键菜单"""

        #创建菜单
        self.popMenu = QMenu()
        #添加菜单选项
        self.popMenu.addAction(QAction(u'修改', self, triggered=self.modify))
        self.popMenu.addAction(QAction(u'删除', self, triggered=self.remove))
        #显示菜单
        self.popMenu.exec_(QCursor.pos())
    #加载数据
    def  load_data(self):
        """加载数据"""

        #获取所有网站
        data=webSiteManager.getAllBase(self.conn)
        #将数据加载到界面上
        self.website_list.setRowCount(len(data))
        #遍历
        for i,item in enumerate(data):
            #设置数据
            self.website_list.setItem(i,0,QTableWidgetItem(str(item[0])))
            self.website_list.setItem(i,1,QTableWidgetItem(item[1]))
            self.website_list.setItem(i,2,QTableWidgetItem(item[2]))

            #1：文本 2：有声
            if  item[3]==1:
                self.website_list.setItem(i,3,QTableWidgetItem('文本'))
            else:
                self.website_list.setItem(i,3,QTableWidgetItem('有声'))
            self.website_list.setItem(i,4,QTableWidgetItem(item[4]))

    def register_event(self):
        """注册事件"""
        self.add_website_button.clicked.connect(self.add_website)
    def add_website(self):
        """添加网站"""
        
        self.addWebSiteSignal.emit()