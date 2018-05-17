from src.entity.zhunkehuPage import zhunkehuPage
from src.functions.LoginAction import *
from time import sleep
class zhunkehuAction(object):
    @staticmethod
    def add_zhunkehuAction(driver,name,datas):
        zhunkehu = zhunkehuPage(driver)
        zhunkehu.clicks().click() # 首页点击准客户管理
        sleep(3)
        zhunkehu.add_button().click()  # 点击新增
        sleep(1)
        zhunkehu.add_Name().send_keys(name)  # 输入姓名
        sleep(1)
        zhunkehu.add_Birthday().send_keys(datas)  # 点击出生日期
        sleep(1)
        zhunkehu.add_work().click()  # 职业代码
        sleep(1)
        zhunkehu.add_work_one().click()   # 职业代码一层
        sleep(1)
        zhunkehu.add_work_one_one().click()  #职业代码二层
        sleep(1)
        zhunkehu.add_work_one_one_one().click()  # 职业代码三层
        sleep(1)
        zhunkehu.add_work_one_one_sure().click()   # 职业代码点击确定
        sleep(1)
        zhunkehu.add_term_of_validity().click()    # 证件有效期
        zhunkehu.add_HealthFlag().click()  # 医保标志
        zhunkehu.add_HealthFlags().click()  # 医保选择（是，否）
        zhunkehu.add_saveCustom().click()   # 点击底部确定
        sleep(3)


if __name__ == '__main__':
    from selenium import webdriver
    import time
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=option)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("http://tstmobile.gwcslife.com/NGLife/")
    time.sleep(1)
    LoginAction.login(driver,username="sh0000002",password="Aa111111")
    time.sleep(3)
    zhunkehuAction.add_zhunkehuAction(driver,'lulu','1990-10-10')
    time.sleep(5)

