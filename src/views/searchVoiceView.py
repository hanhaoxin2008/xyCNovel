from PySide6.QtWidgets import QLabel,QWidget,QSizePolicy,QPushButton,QVBoxLayout
from  PySide6.QtCore import Qt
from  PySide6.QtGui import QFont
class searchVoicelView(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.initUI()
    def initUI(self):
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.rootLayout = QVBoxLayout()
        self.rootLayout.setAlignment(Qt.AlignTop)
        self.setLayout(self.rootLayout)
        self.title=QLabel('搜索有声小说')
        #设置字体
        self.title.setFont(self.parent().font())
        #设置字体大小
        self.title.setStyleSheet('font-size:20px')
        self.title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.rootLayout.addWidget(self.title)




