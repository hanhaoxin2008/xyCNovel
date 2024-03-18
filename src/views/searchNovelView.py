from PySide6.QtWidgets import QComboBox ,QHBoxLayout,QLineEdit,QLabel,QWidget,QSizePolicy,QPushButton,QVBoxLayout
from  PySide6.QtCore import Qt
from  PySide6.QtGui import QFont
class searchNovelView(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.initUI()
    def initUI(self):
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.rootLayout)


        self.title=QLabel('搜索小说')
        #设置字体
        self.title.setFont(self.parent().font())
        #设置字体大小
        self.title.setStyleSheet('font-size:20px')
        self.title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.rootLayout.addWidget(self.title)



        self.search_layout = QHBoxLayout()
        self.search_layout.setAlignment(Qt.AlignLeft)
        self.rootLayout.addLayout(self.search_layout)


        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText('请输入小说名')
        #设置高度
        self.search_edit.setFixedHeight(30)
        #设置圆角
        self.search_edit.setStyleSheet('border-radius:5px')
        #设置字体
        self.search_edit.setFont(self.parent().font())
        self.search_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.search_layout.addWidget(self.search_edit)



        self.search_options = QComboBox()
        self.search_options.addItem("全部")
        self.search_options.addItem("作者")
        self.search_options.addItem("书名")
        self.search_options.setFixedHeight(30)
        self.search_options.setFixedWidth(100)
        self.search_options.setContentsMargins(0,0,0,0)
        self.search_options.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.search_layout.addWidget(self.search_options)


