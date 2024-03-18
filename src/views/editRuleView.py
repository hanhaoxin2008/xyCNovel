from PySide6.QtWidgets import QHBoxLayout,QComboBox,QMessageBox,QLineEdit,QScrollArea,QLabel,QWidget,QSizePolicy,QPushButton,QVBoxLayout
from  PySide6.QtCore import Qt,Signal
from src.rule.ruleManager import rulesManager
from src.wins.ruleTestWin import  ruleTestWin
import configparser

#读取配置
config = configparser.ConfigParser()
config.optionxform = str
config.read('config.ini',encoding='utf-8')
RULESPATH = config["CONFIGS"]["RULESPATH"]


class editRuleView(QWidget):
    savaFinish=Signal()
    def __init__(self,parent):


        super().__init__(parent=parent)
        self.isEdit=False
        self.chose_list=["xpath"]

        self.initUI()
        parent.editRuleSignal.connect(self.editRule)
    def initUI(self):
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.rootLayout)

        self.topLayout= QHBoxLayout()
        self.rootLayout.addLayout(self.topLayout)
        self.topLayout.setAlignment(Qt.AlignLeft)

        self.title=QLabel('规则编辑')
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

        """基本信息"""
        #标签
        self.base_area_label = QLabel('基本信息')
        self.base_area_label.setFont(self.parent().font())
        self.base_area_label.setStyleSheet('font-size:15px')
        self.base_area_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.base_area_label)

        #名称
        self.name_label = QLabel('名称')
        self.name_label.setFont(self.parent().font())
        self.name_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.name_label)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('请输入规则名称')
        # 高度
        self.name_edit.setFixedHeight(20)
        # 圆角
        self.name_edit.setStyleSheet('border-radius:5px')
        self.name_edit.setFont(self.parent().font())
        self.name_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.name_edit)

        #描述
        self.desc_label = QLabel('描述')
        self.desc_label.setFont(self.parent().font())
        self.desc_label.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.desc_label)
        self.desc_edit = QLineEdit()
        self.desc_edit.setPlaceholderText('请输入规则描述')
        self.desc_edit.setFixedHeight(20)
        self.desc_edit.setStyleSheet('border-radius:5px')
        self.desc_edit.setFont(self.parent().font())
        self.desc_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.desc_edit)

        """详情页规则"""
        self.d_area_label = QLabel('详情页规则')
        self.d_area_label.setFont(self.parent().font())
        self.d_area_label.setStyleSheet('font-size:15px')
        self.d_area_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.d_area_label)

        #小说名规则
        self.novel_name_label = QLabel('小说名规则')
        self.novel_name_label.setFont(self.parent().font())
        self.novel_name_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.edit_area_layout.addWidget(self.novel_name_label)
        self.novel_name_layout=QHBoxLayout()
        self.novel_name_edit = QLineEdit()
        self.novel_name_edit.setPlaceholderText('请输入小说名规则')
        self.novel_name_edit.setFixedHeight(20)
        self.novel_name_edit.setStyleSheet('border-radius:5px')
        self.novel_name_edit.setFont(self.parent().font())
        self.novel_name_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.novel_name_layout.addWidget(self.novel_name_edit)
        self.novel_name_type_chose =QComboBox()
        self.novel_name_type_chose.setFixedHeight(20)
        self.novel_name_type_chose.setFixedWidth(100)
        self.novel_name_type_chose.setStyleSheet('border-radius:5px')
        self.novel_name_type_chose.setFont(self.parent().font())
        self.novel_name_type_chose.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.novel_name_type_chose.addItems(self.chose_list)
        self.novel_name_layout.addWidget(self.novel_name_type_chose)
        self.edit_area_layout.addLayout(self.novel_name_layout)

        #作者规则
        self.author_name_label = QLabel('作者规则')
        self.author_name_label.setFixedHeight(20)
        self.author_name_label.setFont(self.parent().font())
        self.edit_area_layout.addWidget(self.author_name_label)
        self.author_name_layout = QHBoxLayout()
        self.author_name_edit = QLineEdit()
        self.author_name_edit.setFixedHeight(20)
        self.author_name_edit.setFont(self.parent().font())
        self.author_name_edit.setPlaceholderText('请输入作者规则')
        self.author_name_edit.setStyleSheet('border-radius:5px')
        self.author_name_layout.addWidget(self.author_name_edit)
        self.author_name_type_chose =QComboBox()
        self.author_name_type_chose.setFixedHeight(20)
        self.author_name_type_chose.setFixedWidth(100)
        self.author_name_type_chose.setStyleSheet('border-radius:5px')
        self.author_name_type_chose.setFont(self.parent().font())
        self.author_name_type_chose.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.author_name_type_chose.addItems(self.chose_list)
        self.author_name_layout.addWidget(self.author_name_type_chose)
        self.edit_area_layout.addLayout(self.author_name_layout)

        #简介规则
        self.desc_label = QLabel('简介规则')
        self.desc_label.setFixedHeight(20)
        self.desc_label.setFont(self.parent().font())
        self.edit_area_layout.addWidget(self.desc_label)
        self.desc_edit_layout = QHBoxLayout()
        self.desc_rule_edit = QLineEdit()
        self.desc_rule_edit.setFixedHeight(20)
        self.desc_rule_edit.setFont(self.parent().font())
        self.desc_rule_edit.setStyleSheet('border-radius:5px')
        self.desc_rule_edit.setPlaceholderText('请输入简介规则')
        self.desc_edit_layout.addWidget(self.desc_rule_edit)
        self.desc_type_chose =QComboBox()
        self.desc_type_chose.setFixedHeight(20)
        self.desc_type_chose.setFixedWidth(100)
        self.desc_type_chose.setStyleSheet('border-radius:5px')
        self.desc_type_chose.setFont(self.parent().font())
        self.desc_type_chose.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.desc_type_chose.addItems(self.chose_list)
        self.desc_edit_layout.addWidget(self.desc_type_chose)
        self.edit_area_layout.addLayout(self.desc_edit_layout)

        #最后更新时间规则
        self.last_update_label = QLabel('最后更新时间规则')
        self.last_update_label.setFixedHeight(20)
        self.last_update_label.setFont(self.parent().font())
        self.edit_area_layout.addWidget(self.last_update_label)
        self.last_update_edit_layout = QHBoxLayout()
        self.last_update_edit = QLineEdit()
        self.last_update_edit.setFixedHeight(20)
        self.last_update_edit.setFont(self.parent().font())
        self.last_update_edit.setStyleSheet('border-radius:5px')
        self.last_update_edit.setPlaceholderText('请输入最后更新时间规则')
        self.last_update_edit_layout.addWidget(self.last_update_edit)
        self.edit_area_layout.addLayout(self.last_update_edit_layout)
        self.last_update_type_chose     = QComboBox()
        self.last_update_type_chose.setFixedWidth(100)
        self.last_update_type_chose.setFixedHeight(20)
        self.last_update_type_chose.setFont(self.parent().font())
        self.last_update_type_chose.setStyleSheet('border-radius:5px')
        self.last_update_type_chose.addItems(self.chose_list)
        self.last_update_type_chose.setCurrentIndex(0)
        self.last_update_edit_layout.addWidget(self.last_update_type_chose)


        #最新章节规则
        self.last_chapter_label = QLabel('最新章节规则')
        self.last_chapter_label.setFixedHeight(20)
        self.last_chapter_label.setFont(self.parent().font())
        self.edit_area_layout.addWidget(self.last_chapter_label)
        self.last_chapter_edit_layout = QHBoxLayout()
        self.last_chapter_edit = QLineEdit()
        self.last_chapter_edit.setFixedHeight(20)
        self.last_chapter_edit.setFont(self.parent().font())
        self.last_chapter_edit.setStyleSheet('border-radius:5px')
        self.last_chapter_edit.setPlaceholderText("请输入最新章节规则")
        self.last_chapter_edit_layout.addWidget(self.last_chapter_edit)
        self.last_chapter_type_chose     = QComboBox()
        self.last_chapter_type_chose.setFixedWidth(100)
        self.last_chapter_type_chose.setFixedHeight(20)
        self.last_chapter_type_chose.setFont(self.parent().font())
        self.last_chapter_type_chose.setStyleSheet('border-radius:5px')
        self.last_chapter_type_chose.addItems(self.chose_list)
        self.last_chapter_type_chose.setCurrentIndex(0)
        self.last_chapter_edit_layout.addWidget(self.last_chapter_type_chose)
        self.edit_area_layout.addLayout(self.last_chapter_edit_layout)

        #最新章节链接规则
        self.last_chapter_link_label = QLabel('最新章节链接规则')
        self.last_chapter_link_label.setFont(self.parent().font())
        self.edit_area_layout.addWidget(self.last_chapter_link_label)
        self.last_chapter_link_edit_layout = QHBoxLayout()
        self.last_chapter_link_edit = QLineEdit()
        self.last_chapter_link_edit.setFixedHeight(20)
        self.last_chapter_link_edit.setFont(self.parent().font())
        self.last_chapter_link_edit.setStyleSheet('border-radius:5px')
        self.last_chapter_link_edit.setPlaceholderText('请输入最新章节链接规则')
        self.last_chapter_link_edit_layout.addWidget(self.last_chapter_link_edit)
        self.last_chapter_link_type_chose = QComboBox()
        self.last_chapter_link_type_chose.setFixedWidth(100)
        self.last_chapter_link_type_chose.setFixedHeight(20)
        self.last_chapter_link_type_chose.setFont(self.parent().font())
        self.last_chapter_link_type_chose.setStyleSheet('border-radius:5px')
        self.last_chapter_link_type_chose.setCurrentIndex(0)
        self.last_chapter_link_type_chose.addItems(self.chose_list)
        self.last_chapter_link_edit_layout.addWidget(self.last_chapter_link_type_chose)
        self.edit_area_layout.addLayout(self.last_chapter_link_edit_layout)

        #类型规则
        self.novel_type_label = QLabel('类型规则:')
        self.novel_type_label.setFont(self.parent().font())
        self.edit_area_layout.addWidget(self.novel_type_label)
        self.novel_type_edit_layout = QHBoxLayout()
        self.novel_type_edit = QLineEdit()
        self.novel_type_edit.setFixedHeight(20)
        self.novel_type_edit.setFont(self.parent().font())
        self.novel_type_edit.setStyleSheet('border-radius:5px')
        self.novel_type_edit.setPlaceholderText('请输入类型规则')
        self.novel_type_edit_layout.addWidget(self.novel_type_edit)
        self.novel_type_type_chose = QComboBox()
        self.novel_type_type_chose.setFixedWidth(100)
        self.novel_type_type_chose.setFixedHeight(20)
        self.novel_type_type_chose.setFont(self.parent().font())
        self.novel_type_type_chose.setStyleSheet('border-radius:5px')
        self.novel_type_type_chose.addItems(self.chose_list)
        self.novel_type_type_chose.setCurrentIndex(0)
        self.novel_type_edit_layout.addWidget(self.novel_type_type_chose)
        self.edit_area_layout.addLayout(self.novel_type_edit_layout)





        #测试按钮
        self.detail_test_button = QPushButton('测试')
        self.detail_test_button.setObjectName('detail_test_button')
        self.detail_test_button.setFixedSize(40,20)
        self.detail_test_button.setFont(self.parent().font())
        self.detail_test_button.setStyleSheet('border-radius:5px')
        self.edit_area_layout.addWidget(self.detail_test_button)
        self.detail_test_button.clicked.connect(self.test_detail_rule)

        #类型规则

    def  test_detail_rule(self):
        rule=self.get_rule()["detail_rule"]
        if not rule == None:
            self.testWin = ruleTestWin("detail",rule)
            self.testWin.show()
    def save(self):
        name = self.name_edit.text()
        desc = self.desc_edit.text()
        if name == '':
            QMessageBox.warning(self, '警告', '请输入规则名称')
            return
        if desc == '':
            QMessageBox.warning(self, '警告', '请输入规则描述')
            return
        if rulesManager.isExist(RULESPATH, name):
            QMessageBox.warning(self, '警告', '规则名称已存在')
            return
        rule=self.get_rule()
        rule["desc"]=desc

        if  rulesManager.addRule(RULESPATH,name,rule):
            QMessageBox.information(self, '提示', '规则添加成功')
            self.savaFinish.emit()
            self.close()
        else:
            QMessageBox.warning(self, '警告', '规则添加失败')
    def get_rule(self):

        rule={}
        #名称规则
        name_rule = {}
        name_rule["type"]=self.novel_name_type_chose.currentText()
        name_rule["value"]=self.novel_name_edit.text()

        #作者规则
        author_rule = {}
        author_rule["type"]=self.author_name_type_chose.currentText()
        author_rule["value"]=self.author_name_edit.text()

        #最后更新
        last_update_rule = {}
        last_update_rule["type"]=self.last_update_type_chose.currentText()
        last_update_rule["value"]=self.last_update_edit.text()

        #最新章节
        last_chapter_rule = {}
        last_chapter_rule["type"]=self.last_chapter_type_chose.currentText()
        last_chapter_rule["value"]=self.last_chapter_edit.text()

        #最新章节链接
        last_chapter_link_rule = {}
        last_chapter_link_rule["type"]=self.last_chapter_link_type_chose.currentText()
        last_chapter_link_rule["value"]=self.last_chapter_link_edit.text()

        desc_rule = {}
        desc_rule["type"]=self.desc_type_chose.currentText()
        desc_rule["value"]=self.desc_rule_edit.text()

        type_rule={}
        type_rule["type"]=self.novel_type_type_chose.currentText()
        type_rule["value"]=self.novel_type_edit.text()

        #检查是否为空
        if name_rule["value"] == '':
            QMessageBox.warning(self, '警告', '请输入小说名称规则')
            return

        detail_rule={}
        detail_rule["name"]=name_rule
        detail_rule["author"]=author_rule
        detail_rule["update"]=last_update_rule
        detail_rule["last"]=last_chapter_rule
        detail_rule["last_href"]=last_chapter_link_rule
        detail_rule["type"]=type_rule
        detail_rule["desc"]=desc_rule

        rule["detail_rule"]=detail_rule

        return rule
    def editRule(self,name):
        #设置名称
        self.name_edit.setText(name)
        #获取规则
        rule=rulesManager.getByName(RULESPATH,name)
        #设置简介
        self.desc_edit.setText(rule["desc"])

        """设置详情规则"""
        detail_rule=rule["detail_rule"]
        self.novel_name_type_chose.setCurrentText(detail_rule["name"]["type"])
        self.novel_name_edit.setText(detail_rule["name"]["value"])

        self.author_name_type_chose.setCurrentText(detail_rule["author"]["type"])
        self.author_name_edit.setText(detail_rule["author"]["value"])

        self.last_update_type_chose.setCurrentText(detail_rule["update"]["type"])
        self.last_update_edit.setText(detail_rule["update"]["value"])

        self.last_chapter_type_chose.setCurrentText(detail_rule["last"]["type"])
        self.last_chapter_edit.setText(detail_rule["last"]["value"])

        self.last_chapter_link_type_chose.setCurrentText(detail_rule["last_href"]["type"])
        self.last_chapter_link_edit.setText(detail_rule["last_href"]["value"])

        self.novel_type_type_chose.setCurrentText(detail_rule["type"]["type"])
        self.novel_type_edit.setText(detail_rule["type"]["value"])

        self.desc_type_chose.setCurrentText(detail_rule["desc"]["type"])
        self.desc_rule_edit.setText(detail_rule["desc"]["value"])
