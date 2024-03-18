import json


class rulesManager:



    @staticmethod
    def open_rules(path):
        with open(path+"rules.json", 'r',encoding="utf-8") as file:
            data = json.load(file)
        return data
    @staticmethod
    def write_rules(path,data):
        with open(path+"rules.json", 'w',encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    @staticmethod
    def get(path,name):
        data = rulesManager.open_rules(path)
        try:
            return data[name]
        except:
            return None
    @staticmethod
    def getAll(path):
        all=[]
    @staticmethod
    def getRuel(path,name):
        data = rulesManager.open_rules(path)
        try:
            return data[name]
        except:
            return None
    @staticmethod
    def getAll(path):
        all=[]
        data = rulesManager.open_rules(path)
        for i in data:
            all.append({i:data[i]})
        return  all
    @staticmethod
    def getByName(path,name):
        data=rulesManager.open_rules(path)[name]
        return data
    @staticmethod
    def addRule(path,name,rule):
        try:
            data = rulesManager.open_rules(path)
            data[name]=rule
            rulesManager.write_rules(path=path,data=data)
            return True
        except:
            return False

    @staticmethod
    def isExist(path,name):
        data = rulesManager.open_rules(path)
        if name in data:
            return True
        else:
            return False
    @staticmethod
    def deleteRule(path,name):
        try:
            data = rulesManager.open_rules(path)
            if name in data:
                del data[name]
                rulesManager.write_rules(path=path,data=data)
                return True
            else:
                return False
        except Exception as e:
            return False
