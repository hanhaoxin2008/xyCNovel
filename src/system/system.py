from  PySide6.QtGui import QFontDatabase

class system:
    @staticmethod
    #获取系统所有字体
    def get_all_fonts():
        """获取系统的所有字体"""
        fonts = QFontDatabase.families()
        return fonts