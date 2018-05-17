from selenium import webdriver
from src.functions.LoginAction import LoginAction
import ddt, unittest
from config.Log import *
from src.common.testDataMap import testDataMap

@ddt.ddt
class changsheng(unittest.TestCase):
    logger.info("长生项目建议书测试开始")
    def setUp(self):
            logger.info("开始初始化浏览器.....")
            option = webdriver.ChromeOptions()
            # option.add_argument('headless')  # 静默执行，不打开浏览器
            option.add_argument('disable-infobars')  # 取消打开浏览器时候提示‘被自动化控制’等字体
            self.driver = webdriver.Chrome(chrome_options=option)   # 实例化浏览器
            self.driver.implicitly_wait(20)   # 隐式等待
            self.driver.get("http://tstmobile.gwcslife.com/NGLife/")
            self.driver.maximize_window()  # 最大化浏览器

    testdata = testDataMap()  # 实例化读取Excel数据操作
    @ddt.data(*testdata)
    def test_01(self,data):
        print('---登录操作---')
        print('账号:' + data['userName'], '密码:' + data['passWord'])
        logger.info('输入账号密码,开始登录.........................................')
        LoginAction.login(self.driver, data['userName'], data['passWord'])  # 调用登录的方法
        self.assertEqual(data['element'], self.driver.title)  # Excel中的预期结果和页面信息作比较
        logger.info('账号:%s,密码:%s' % (data['userName'], data['passWord']))
        logger.info('登录操作结束..................................................')
        # logger.info('点击建议书操作开始............................................')
        # jianyishuAction.click_jianyishu(self.driver)
        # logger.info('点击建议书操作结束............................................')
        # self.driver.save_screenshot(img)


