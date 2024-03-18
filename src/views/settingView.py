from PySide6.QtWidgets import QComboBox,QScrollArea,QLabel,QWidget,QSizePolicy,QVBoxLayout
from  PySide6.QtCore import Qt,Signal
from PySide6.QtGui import QFontDatabase
from src.setting.settingManager import settingManager
from src.system.system import system
import configparser
#读取配置
config = configparser.ConfigParser()
config.optionxform = str
config.read('config.ini',encoding='utf-8')
SETTINGSPATH=config['CONFIGS']['SETTINGSPATH']

class settingView(QWidget):
    settingChanged = Signal()

    def __init__(self,parent):
        super().__init__(parent=parent)
        self.setting()
        self.initUI()

    def initUI(self):
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.rootLayout)
        self.title=QLabel('软件设置')
        #设置字体
        self.title.setFont(self.parent().font())
        #设置字体大小
        self.title.setStyleSheet('font-size:20px')
        self.title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.rootLayout.addWidget(self.title)


        self.edit_area =  QScrollArea()
        self.edit_area.setWidgetResizable(True)
        self.edit_area.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.edit_area_layout = QVBoxLayout()
        self.edit_area_layout.setAlignment(Qt.AlignTop)
        self.edit_area.setLayout(self.edit_area_layout)
        self.rootLayout.addWidget(self.edit_area)

        """界面设置区域"""
        #标签
        self.ui_area_label = QLabel('界面设置')
        self.ui_area_label.setFont(self.parent().font())
        self.ui_area_label.setStyleSheet('font-size:15px')
        self.ui_area_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.ui_area_label)

        #主题
        self.theme_label = QLabel('主题')
        self.theme_label.setFont(self.parent().font())
        self.theme_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.theme_label)
        self.theme_chose = QComboBox()
        self.theme_chose.addItem("grey")
        self.theme_chose.addItem("red")
        #设置默认
        self.theme_chose.setCurrentText(self.theme)
        self.theme_chose.setFixedHeight(30)
        self.theme_chose.setFixedWidth(200)
        self.theme_chose.setContentsMargins(0, 0, 0, 0)
        self.theme_chose.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.theme_chose)
        #下拉框更改事件
        self.theme_chose.currentIndexChanged.connect(self.chose_change(self.theme_chose,"ui","theme_name"))

        #字体
        self.font_label = QLabel('字体')
        self.font_label.setFont(self.parent().font())
        self.font_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.font_label)
        self.font_chose = QComboBox()
        for font in system.get_all_fonts():
            self.font_chose.addItem(font)
        self.font_chose.setCurrentText(settingManager.get_ui_font_name(SETTINGSPATH))
        self.font_chose.setFixedHeight(30)
        self.font_chose.setFixedWidth(200)
        self.font_chose.setContentsMargins(0, 0, 0, 0)
        self.font_chose.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.font_chose)
        # 下拉框更改事件
        self.font_chose.currentIndexChanged.connect(self.chose_change(self.font_chose,"ui", "font_name"))

    def chose_change(self,chose,group,setting):
        def change(evnet):
            #获取当前的选择
            change_value = chose.currentText()
            self.change_setting(group,setting,change_value)
        return change
    #更改设置
    def  change_setting(self,group,setting,value):
        settingManager.set(SETTINGSPATH,group,setting,value)
        self.settingChanged.emit()

    def setting(self):
        self.theme = settingManager.get_ui_theme_name(SETTINGSPATH)




