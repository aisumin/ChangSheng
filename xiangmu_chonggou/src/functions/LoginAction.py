'''
组装登录的模块
'''
from src.entity.LoginPage import LoginPage
import time
class LoginAction(object):
    @staticmethod
    def login(driver,username,password):
        try:
            login = LoginPage(driver)
            login.userNameObj().send_keys(username)
            login.passwordObj().send_keys(password)
            login.loginButton().click()
            time.sleep(5)
        except Exception as e:
            raise e




