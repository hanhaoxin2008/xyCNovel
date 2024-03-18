#使用xpath
from lxml import etree
import requests

def get_html(url,header={}):

    header=header
    html=requests.get(url,headers=header)
    return html.text

#获取详情类
class  Detail:
    def __init__(self,url,rules):
        self.url = url

        if  rules is {}:
            raise ValueError('rules is null')
        if  rules["name"]=="":
            raise ValueError('rules must has name')
        self.name_rule = rules['name']["value"]
        self.author_rule = rules['author']["value"]
        self.desc_rule = rules['desc']["value"]
        self.type_rule = rules['type']["value"]
        self.update_rule=rules['update']["value"]
        self.last_rule=rules['last']["value"]
        self.last_href_rule=rules['last_href']["value"]
    def get(self):
        html=get_html(self.url)
        etree.HTML(html)
        try:
            name=etree.HTML(html).xpath(self.name_rule)[0]
        except:
            name="未知"
        try:
            author=etree.HTML(html).xpath(self.author_rule)[0]
        except:
            author="未知"
        try:
            desc=etree.HTML(html).xpath(self.desc_rule)[0]
        except:
            desc="未知"
        try:
            type=etree.HTML(html).xpath(self.type_rule)[0]
        except:
            type="未知"
        try:
            update=etree.HTML(html).xpath(self.update_rule)[0]
        except:
            update="未知"
        try:
            last=etree.HTML(html).xpath(self.last_rule)[0]
        except:
            last="未知"
        try:
            last_href=etree.HTML(html).xpath(self.last_href_rule)[0]
        except:
            last_href="未知"

        return {
            'name':name,
            'author':author,
            'desc':desc,
            'type':type,
            'update':update,
            'last':last,
            'last_href':last_href
        }



