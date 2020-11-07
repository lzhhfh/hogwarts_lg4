import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_case(self):
        db = shelve.open('cookies')
        #本地cookies读取保存的cookie数据库
        cookies = db['cookie']
        db.close()
        #打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            print('debug', cookie)
            self.driver.add_cookie(cookie)
        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        # 点击【添加成员】
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        # 输入姓名
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("aaaaa")
        # 输入账号
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys("666666")
        #输入手机号码
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_phone").send_keys("13566666666")
        #点击保存
        self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar:nth-child(3) > .js_btn_save").click()
        # 断言添加的成员与实际的成员名一致
        result = self.driver.find_element(By.CSS_SELECTOR, "#member_list > tr:nth-child(1) > td:nth-child(2) > span").text
        assert "aaaaa" == result
        sleep(5)