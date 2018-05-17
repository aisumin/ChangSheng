from src.common.ObjectMap import *
from src.common.ParseConfigurationFile import ParseCofigFile
class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.loginOptions = self.parseCF.getItemsSection("changsheng_login")
    def userNameObj(self):
        try:
            locateType,locatorExperession = self.loginOptions["loginpage.username".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def passwordObj(self):
        try:
            locateType,locatorExperession = self.loginOptions["loginpage.password".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatorExperession)
            return elementObj
        except Exception as e:
            raise e
    def loginButton(self):
        try:
            locateType, locatoeExpression = self.loginOptions["loginpage.loginbutton".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locatoeExpression)
            return elementObj
        except Exception as e:
            raise e


