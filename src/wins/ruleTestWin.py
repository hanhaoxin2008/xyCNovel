from PySide6 .QtWidgets import QSizePolicy,QTextEdit,QLineEdit,QLabel, QMessageBox,QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QFont,QIcon
from src.setting.settingManager import settingManager
import configparser
import sys
from src.reptile.reptile import Detail
#读取配置
config = configparser.ConfigParser()
config.optionxform = str
config.read('config.ini',encoding='utf-8')
STYLEPATH = config['CONFIGS']['STYLEPATH']
SETTINGSPATH=config['CONFIGS']['SETTINGSPATH']
class ruleTestWin(QMainWindow):
    def __init__(self,type,rule):
        super().__init__()
        self.type=type
        self.rule=rule
        self.setting()
        self.initUI()
    def initUI(self):
        self.qss=self.getQss(self.theme)
        self.setStyleSheet(self.qss)
        self.setCentralWidget(QWidget())
        self.setWindowIcon(QIcon('xyCNovel.png'))

        self.setWindowTitle('测试')


        self.root_layout = QVBoxLayout()
        self.centralWidget().setLayout(self.root_layout)

        self.label1=QLabel()
        self.label1.setText('输入')
        self.root_layout.addWidget(self.label1)

        self.inputLine= QLineEdit()
        self.inputLine.setPlaceholderText('请输入')
        self.inputLine.setStyleSheet('border-radius:5px')
        self.root_layout.addWidget(self.inputLine)

        self.label2=QLabel()
        self.label2.setText('输出')
        self.root_layout.addWidget(self.label2)

        self.outputText= QTextEdit()
        self.outputText.setReadOnly(True)
        self.outputText.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.root_layout.addWidget(self.outputText)


        self.testButton=QPushButton('测试')
        self.testButton.setObjectName('testButton')
        self.testButton.clicked.connect(self.test)
        self.root_layout.addWidget(self.testButton)
    def setting(self):
        self.theme=settingManager.get_ui_theme_name(SETTINGSPATH)
        self.setFont(QFont(settingManager.get_ui_font_name(SETTINGSPATH)))
    def getQss(self,theme):
        try:
            qss=open(STYLEPATH+"style"+"_"+theme+".qss", "r").read()
            return qss
        except:
            QMessageBox.warning(self, "警告", "找不到样式文件")
            sys.exit()
    def test(self):
        #检查输入


        if self.inputLine.text()=='':
            QMessageBox.warning(self, "警告", "输入不能为空")
            return

        try:
            if self.type=="detail":
                t = Detail(self.inputLine.text(), self.rule)
                data=t.get()
                # 显示信息
                text=""
                for key in data.keys():
                    text+=key+":"+data[key]+"\n"
                self.outputText.setText(text)

        except Exception as e:
            self.outputText.setText(e.__str__())
