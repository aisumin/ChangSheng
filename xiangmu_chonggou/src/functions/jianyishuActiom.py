from src.entity.jianyishuPage import jianyishuPage
from src.functions.LoginAction import *
from time import sleep
class jianyishuAction(object):
    @staticmethod
    def click_jianyishu(driver,name,datas):
        try:
            jianyishu = jianyishuPage(driver)
            jianyishu.clicks().click()
            sleep(5)
            jianyishu.adduser().click()
            sleep(3)
            jianyishu.bbr_name().send_keys(name)
            sleep(1)
            jianyishu.bbr_sex_g().click()
            sleep(1)
            jianyishu.bbr_from().send_keys(datas)
            sleep(1)
            jianyishu.bbr_work().click()
            sleep(1)
            jianyishu.bbr_work_one().click()
            sleep(1)
            jianyishu.bbr_work_one_one().click()
            sleep(1)
            jianyishu.bbr_work_one_one_one().click()
            sleep(1)
            jianyishu.bbr_work_one_one_sure().click()
            sleep(1)
            jianyishu.bbr_beibaoren().click()
            sleep(1)
            jianyishu.bbr_beibaoren_guanxi().click()
            sleep(1)
            jianyishu.bbr_next().click()
            sleep(10)

        except Exception as e:
            print('click_jianyishu error:%s' %e)

if __name__== '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("http://tstmobile.gwcslife.com/NGLife/")
    time.sleep(5)
    LoginAction.login(driver,username="sh0000002",password="Aa111111")
    time.sleep(3)
    jianyishuAction.click_jianyishu(driver,'zhaoli','1990-10-10')
    time.sleep(10)




