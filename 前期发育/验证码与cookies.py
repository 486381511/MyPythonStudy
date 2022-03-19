import requests
from lxml import etree
from chaojiying import Chaojiying_Client

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
        (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
url_get = requests.get(url=url, headers=headers)
url_get.encoding = 'utf-8'

zhaoerweima = etree.HTML(url_get.text)
erweima_list = zhaoerweima.xpath('//*[@id="imgCode"]/@src')[0]
erweima_url = 'https://so.gushiwen.cn'+erweima_list

get_erweima_file = requests.get(url=erweima_url, headers=headers).content
with open('.\\cc.jpg', 'wb') as fn:
    fn.write(get_erweima_file)

see_erweima = Chaojiying_Client('lym104432061', '104432061love', '929596')
im = open('cc.jpg', 'rb').read()
code_erweima = see_erweima.PostPic(im, 1004)['pic_str']
print(code_erweima)

#模拟登录
#抓包请求
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data = {
    '__VIEWSTATE':"c3zTp4sF0uJInN0oCrM80xrrvA7yqlOQM7QRWKg9oM6kMAYreKGvg0WsrFwPORqob4dicYc19mf4C5SMaAMUYD5/Upj6UH6Dtc27H+ctA6//SA2COGkkLAM3uwo=",
    '__VIEWSTATEGENERATOR':"C93BE1AE",
    'from':"http://so.gushiwen.cn/user/collect.aspx",
    'email':"486381511@qq.com",
    'pwd':"104432061love",
    'code':code_erweima,
    'denglu':"登录",
}

use_url = requests.post(url=post_url, data=data, headers=headers)
use_url.encoding = 'utf-8'
with open('.\\shichi.html', 'w', encoding='utf-8') as fp:
    fp.write(use_url.text)




#验证码与post不一一对应？？？？？？？
#不知道哪里出现了bug？？？？？？？？？