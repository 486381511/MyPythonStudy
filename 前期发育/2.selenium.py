from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象
bro = webdriver.Chrome()
#打开指定url
bro.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')
#获取当前url源码

email = bro.find_element_by_id('email')
email.send_keys('486381511@qq.com')

pwd = bro.find_element_by_id('pwd')
pwd.send_keys('104432061love')

sleep(1)

denglu = bro.find_element_by_id('denglu')
denglu.click()

sleep(2)

quit()