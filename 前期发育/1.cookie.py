import requests


#cookie手动输入，写入头信息里面
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
        (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
           'Cookie': 'ASP.NET_SessionId=nrykvbj04pvi5urll4cis11k; codeyzgswso=99a9f44b2926d222; wsEmail=486381511%40qq.com; gsw2017user=2521282%7c65425E480214C7ED4C8F396AABA8E53C; login=flase; wxopenid=defoaltid; gswZhanghao=486381511%40qq.com; gswEmail=486381511%40qq.com'
           }
url = 'https://so.gushiwen.cn/user/collect.aspx'
detail_url = requests.get(url=url, headers=headers)
detail_url.encoding = 'utf-8'
with open('.\\shichi.html','w',encoding='utf-8') as fp:
    fp.write(detail_url.text)



