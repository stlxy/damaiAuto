"""
基于python和selenium实现的大麦网自动刷新抢票脚本
用户要提前添加好个人信息和收货地址
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 设置抢票链接和开票时间

# URL = "https://piao.damai.cn/146290.html?spm=a2o6e.search.0.0.7e2b4d157EDtjL"# PC页面

URL = 'https://m.damai.cn/damai/detail/item.html?itemId=593131142099'#手机页面
# HOUR = 13
MIN  = 0
USERNAME = "stlxy44"

driver = webdriver.Chrome()
# 设置等待时间
wait = WebDriverWait(driver, 5)
driver.get(URL)

"""
移动端抢票操作
"""

def login_mobile():
    """
    点击购买进入登录界面
    自行输入帐号密码
    """
    # 立即购买
    buybtn = None
    while None == buybtn:
        buybtn = choose('/html/body/div[1]/div[2]/div/div[1]/div[2]/div')
    driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
    buybtn.click()
    # 默认已经选好时间了，再点击立即购买
    buy = None
    while None == buy:
        buy = choose('/html/body/div[1]/div[3]/div[2]/div[1]/div')
    driver.execute_script("arguments[0].scrollIntoView();", buy) 
    buy.click()

def buy_mobile():
    try:
        # 立即购买
        buybtn = None
        while None == buybtn:
            buybtn = choose('/html/body/div[1]/div[2]/div/div[1]/div[2]/div')
        driver.execute_script("arguments[0].scrollIntoView();", buybtn) 
        buybtn.click()
        # 默认已经选好时间了，再点击立即购买
        buy = None
        while None == buy:
            buy = choose('/html/body/div[1]/div[3]/div[2]/div[1]/div')
        driver.execute_script("arguments[0].scrollIntoView();", buy) 
        buy.click()
        # 580票面
        price = None
        while None == price:
            price = choose('//html/body/div[1]/div/div[2]/ul/li[5]')
        driver.execute_script("arguments[0].scrollIntoView();", price) 
        price.click()
        # 数量+1
        count = None
        while None == count:
            count = choose('/html/body/div[1]/div/div[3]/ul/li/div/div[3]')
        driver.execute_script("arguments[0].scrollIntoView();", count) 
        count.click()
        # 选好了
        select = None
        while None == select:
            select = choose('/html/body/div[1]/div/div[4]/div[3]')
        driver.execute_script("arguments[0].scrollIntoView();", select) 
        select.click()
        # 购票人
        booker = None
        while None == booker:
            booker = choose('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/ul/li/div')
        driver.execute_script("arguments[0].scrollIntoView();", booker) 
        booker.click()
        # 去付款
        pay = None
        while None == pay:
            pay = choose('/html/body/div[1]/div[2]/div[2]/div[2]/div')
        driver.execute_script("arguments[0].scrollIntoView();", pay) 
        pay.click()
    except Exception:
        print("抢票失败，尝试重新抢票")
        buy_mobile()

def test_mobile():
    login_mobile()
    time.sleep(30)
    print("开始抢票")
    buy_mobile()
    print("抢票成功")

def main():
    # 默认PC网页，手机网页对应修改即可
    login()
    # 30秒等待用户输入密码后再开始刷
    time.sleep(30)
    while 1:
        if MIN == time.localtime().tm_min:
            print("开始抢票")
            buy()
            print("抢票成功")

if __name__ == '__main__':
    # test()
    test_mobile()
    # main()
