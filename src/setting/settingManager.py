import json
class settingManager:
    @staticmethod
    def openSetting(path):
        with open(path+"setting.json", 'r',encoding="utf-8") as file:
            data = json.load(file)
        return data
    @staticmethod
    def writeSettings(path,data):
        with open(path+"setting.json", 'w',encoding="utf-8") as file:
            json.dump(data, file)

    @staticmethod
    def get(path,group,name):
        return settingManager.openSetting(path)[group][name]
    @staticmethod
    def getUiGroup(path,name):
        return settingManager.get(path,"ui",name)
    @staticmethod
    def get_ui_theme_name(path):
        return  settingManager.getUiGroup(path,"theme_name")
    @staticmethod
    def get_ui_font_name(path):
        return  settingManager.getUiGroup(path,"font_name")
    @staticmethod
    def set(path,group,name,value):
        data=settingManager.openSetting(path)
        data[group][name]=value
        settingManager.writeSettings(path,data)

