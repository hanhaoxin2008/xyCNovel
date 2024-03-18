from PySide6.QtWidgets import QMessageBox, QAbstractItemView, QMenu, QHeaderView, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QLabel, QWidget, QSizePolicy, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QCursor, QAction
from src.rule.ruleManager import rulesManager
import configparser

# 读取配置
config = configparser.ConfigParser()
config.optionxform = str
config.read('config.ini', encoding='utf-8')
RULESPATH = config["CONFIGS"]["RULESPATH"]


class rulesManagerView(QWidget, QObject):
    addRuleSignal = Signal()
    editRuleSignal = Signal(str)

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.initUI()
        self.register_event()
        self.load_data()

    def initUI(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.rootLayout)

        self.toplayout = QHBoxLayout()
        self.rootLayout.addLayout(self.toplayout)
        self.toplayout.setAlignment(Qt.AlignLeft)

        self.title = QLabel('规则管理')
        # 设置字体
        self.title.setFont(self.parent().font())
        # 设置字体大小
        self.title.setStyleSheet('font-size:20px')
        self.title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.toplayout.addWidget(self.title)

        self.add_rule_button = QPushButton('添加网站')
        self.add_rule_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.add_rule_button.setObjectName('add_rule_button')
        self.add_rule_button.setFixedSize(100, 30)
        self.toplayout.addWidget(self.add_rule_button)

        # 网站列表
        self.rul_list = QTableWidget()
        self.rul_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.rul_list.setFont(self.parent().font())
        self.rul_list.setStyleSheet('font-size:15px')
        self.rul_list.setObjectName('rul_list')
        self.rootLayout.addWidget(self.rul_list)
        # 表头
        self.rul_list.setColumnCount(2)
        self.rul_list.setHorizontalHeaderLabels(['名称',"描述"])
        # 设置列可拉伸
        self.rul_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 隐藏左边序号
        self.rul_list.verticalHeader().setVisible(False)
        # 设置不可编辑
        self.rul_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 自定义表项右键菜单
        self.rul_list.setContextMenuPolicy(Qt.CustomContextMenu)
        # 设置一次只能选中一行
        self.rul_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.rul_list.customContextMenuRequested.connect(self.show_menu)
        self.rul_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.rul_list.setAlternatingRowColors(True)
        self.rul_list.setSortingEnabled(False)
        self.rul_list.sortByColumn(0, Qt.AscendingOrder)

    def remove(self):
        """删除"""
        # 确认删除
        reply = QMessageBox.question(self, '删除', '是否删除', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        # 获取选中行选中行
        row = self.rul_list.currentIndex().row()
        # 获取name
        name = self.rul_list.item(row, 0).text()

        if rulesManager.deleteRule(RULESPATH,name):
            QMessageBox.information(self, '删除', '删除成功', QMessageBox.Ok)
            # 删除界面中对应行
            self.rul_list.removeRow(row)
        else:
            QMessageBox.information(self, '删除', '删除失败', QMessageBox.Ok)

    def modify(self):
        """修改"""
        # 获取选中行
        row = self.rul_list.currentIndex().row()
        name = self.rul_list.item(row, 0).text()


        self.editRuleSignal.emit(name)

    def show_menu(self, event):
        """右键菜单"""

        # 创建菜单
        self.popMenu = QMenu()
        # 添加菜单选项
        self.popMenu.addAction(QAction(u'修改', self, triggered=self.modify))
        self.popMenu.addAction(QAction(u'删除', self, triggered=self.remove))
        # 显示菜单
        self.popMenu.exec_(QCursor.pos())

    # 加载数据
    def load_data(self):
        data=rulesManager.getAll(RULESPATH)
        self.rul_list.setRowCount(len(data))
        for i,item in enumerate(data):
            #获取item的第一个key
            key=list(item.keys())[0]
            self.rul_list.setItem(i, 0, QTableWidgetItem(key))
            description=item[key]["desc"]
            self.rul_list.setItem(i, 1, QTableWidgetItem(description))
    def register_event(self):
        """注册事件"""
        self.add_rule_button.clicked.connect(self.add_rule)

    def add_rule(self):
        """添加网站"""

        self.addRuleSignal.emit()