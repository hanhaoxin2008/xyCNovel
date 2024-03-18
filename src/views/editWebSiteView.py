from PySide6.QtWidgets import QHBoxLayout,QComboBox,QMessageBox,QLineEdit,QScrollArea,QLabel,QWidget,QSizePolicy,QPushButton,QVBoxLayout
from  PySide6.QtCore import Qt,QUrl,Signal
from  PySide6.QtGui import QDesktopServices
from src.webSiteManager.webSiteManager import webSiteManager
from src.rule.ruleManager import rulesManager
import configparser

#读取配置
config = configparser.ConfigParser()
config.optionxform = str
config.read('config.ini',encoding='utf-8')
DATAPATH = config["CONFIGS"]["DATAPATH"]
RULESPATH = config["CONFIGS"]["RULESPATH"]


class editWebSiteView(QWidget):
    savaFinish=Signal()
    def __init__(self,parent):


        super().__init__(parent=parent)
        self.isEdit=False
        allrule=rulesManager.getAll(RULESPATH)
        self.rule_list=[]
        for  rule in allrule:
            self.rule_list.append(list(rule.keys())[0])

        self.initUI()
        self.conn=webSiteManager.init(DATAPATH)

        parent.editWebSiteSignal.connect(self.editWebSite)

    def initUI(self):
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.rootLayout)

        self.topLayout= QHBoxLayout()
        self.rootLayout.addLayout(self.topLayout)
        self.topLayout.setAlignment(Qt.AlignLeft)

        self.title=QLabel('网站编辑')
        #设置字体
        self.title.setFont(self.parent().font())
        #设置字体大小
        self.title.setStyleSheet('font-size:20px')
        self.title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.topLayout.addWidget(self.title)


        #保存按钮
        self.save_btn = QPushButton('保存')
        self.save_btn.setObjectName('save_btn')
        self.save_btn.setFont(self.parent().font())
        self.save_btn.setFixedSize(60,30)
        self.save_btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.topLayout.addWidget(self.save_btn)
        self.save_btn.clicked.connect(self.save)


        self.edit_area =  QScrollArea()
        self.edit_area.setWidgetResizable(True)
        self.edit_area.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.edit_area_layout = QVBoxLayout()
        self.edit_area_layout.setAlignment(Qt.AlignTop)
        self.edit_area.setLayout(self.edit_area_layout)
        self.rootLayout.addWidget(self.edit_area)

        """基本信息区域"""
        #标签
        self.base_area_label = QLabel('基本信息')
        self.base_area_label.setFont(self.parent().font())
        self.base_area_label.setStyleSheet('font-size:15px')
        self.base_area_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.base_area_label)


        #网站名称
        self.name_label = QLabel('网站名称')
        self.name_label.setFont(self.parent().font())
        self.name_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.name_label)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('请输入网站名称')
        #高度
        self.name_edit.setFixedHeight(20)
        #圆角
        self.name_edit.setStyleSheet('border-radius:5px')
        self.name_edit.setFont(self.parent().font())
        self.name_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.name_edit)



        #网站地址
        self.url_label = QLabel('网站地址')
        self.url_label.setFont(self.parent().font())
        self.url_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.url_label)
        self.url_edit = QLineEdit()
        #提示文本
        self.url_edit.setPlaceholderText('请输入网站地址')
        #高度
        self.url_edit.setFixedHeight(20)
        #圆角
        self.url_edit.setStyleSheet('border-radius:5px')
        self.url_edit.setFont(self.parent().font())
        self.url_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.url_edit)

        #打开链接按钮
        self.open_btn = QPushButton('打开')
        self.open_btn.setObjectName('open_btn')
        self.open_btn.setFont(self.parent().font())
        self.open_btn.setFixedSize(40,20)
        self.open_btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.open_btn.clicked.connect(self.open_url)
        self.edit_area_layout.addWidget(self.open_btn)

        #类型
        self.type_label = QLabel('类型')
        self.type_label.setFont(self.parent().font())
        self.type_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.type_label)

        #下拉框
        self.type_combo = QComboBox()
        self.type_combo.addItem("文本")
        self.type_combo.addItem("有声")
        self.type_combo.setFixedHeight(20)
        self.type_combo.setFont(self.parent().font())
        self.type_combo.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.type_combo)

        """高级"""
        self.advanced_label = QLabel('高级')
        self.advanced_label.setStyleSheet('font-size:15px')
        self.advanced_label.setFont(self.parent().font())
        self.advanced_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.advanced_label)

        #使用的规则
        self.rule_label = QLabel('规则')
        self.rule_label.setFont(self.parent().font())
        self.rule_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.rule_label)

        self.rule_chose=QComboBox()
        self.rule_chose.setFixedHeight(20)
        self.rule_chose.setFont(self.parent().font())
        self.rule_chose.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.rule_chose.addItems(self.rule_list)
        self.edit_area_layout.addWidget(self.rule_chose)


    def open_url(self):
        """打开链接"""
        url = self.url_edit.text()
        if url:
            QDesktopServices.openUrl(QUrl(url))
        else:
            QMessageBox.warning(self,'警告','请输入网站地址')
    def save(self):

        url = self.url_edit.text()
        rule=self.rule_chose.currentText()
        #验证url是否有效
        if  QUrl(url).isValid():
            name=self.name_edit.text()
            type=int(self.type_combo.currentIndex())+1
            if url and name:
                #判断模式
                if self.isEdit:
                    #编辑模式
                    webSiteManager.update(self.conn,self.id,name,url,type,rule)
                else:
                    #添加模式
                    webSiteManager.add(self.conn,name,url,type,rule)
                QMessageBox.information(self, '提示', '保存成功')
                self.savaFinish.emit()
                self.close()
            else:
                QMessageBox.warning(self,'警告','请输入网站地址和名称')
        else:
            QMessageBox.warning(self,'警告','请输入有效的网站地址')


    def editWebSite(self,id,name,url,type,rule):
        """编辑网站"""
        #编辑模式
        self.isEdit=True
        #设置文本
        self.url_edit.setText(url)
        self.name_edit.setText(name)
        #获取id
        self.id=id
        if  type=="文本":
            self.type_combo.setCurrentIndex(0)
        elif type=="有声":
            self.type_combo.setCurrentIndex(1)
        self.rule_chose.setCurrentText(rule)