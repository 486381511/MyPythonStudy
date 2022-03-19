import requests
from lxml import etree
import threading
import os
import sys
import shutil
import time
import datetime

def getUrl(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
        (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    getUrl = requests.get(url=url, headers=header)
    getUrl.encoding = 'utf-8'
    return getUrl.text

def findTitle(url,getUrl,yourDir):
    title = etree.HTML(getUrl)
    detailTitle = title.xpath('//div[@id="info"]/h1/text()')[0]
    if os.path.isdir(yourDir+'\\'+detailTitle):
        return detailTitle
    else:
        os.makedirs(yourDir+'\\'+detailTitle)
        return detailTitle

def findZhang(getUrl):
    Zhang = etree.HTML(getUrl)
    unZhangList = Zhang.xpath('//*[@id="list"]//a/@href')
    unZhangNameList = Zhang.xpath('//*[@id="list"]//a/text()')
    print('当前小说共有 '+str(len(unZhangNameList)-1)+' 章')
    print('最新的章节是 '+unZhangNameList[-1])
    zhangList = []
    for smallUrl in unZhangList:
        pageUrl = 'https://www.xbiquge.la/' + smallUrl
        zhangList.append(pageUrl)
    return zhangList

def isGenXin(yourDir,name,zhangList):
    dirlist = os.listdir(yourDir+'\\'+name)
    if not len(zhangList) > len(dirlist):
        print('当前章节已经是最新的了，不需要更新')
        sys.exit()
    else:
        Shu = len(dirlist)
        print('当前有 '+str(len(zhangList)-len(dirlist)-1)+' 章，需要更新')
        GenXinList = []
        for i in zhangList[len(dirlist):]:
            GenXinList.append(i)
        return GenXinList,Shu


def findText(detailUrl,i,name,yourDir):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
            (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    findPageText = requests.get(url=detailUrl,headers=header)
    findPageText.encoding = 'utf-8'
    detailTextIng = etree.HTML(findPageText.text)
    detailTitle = detailTextIng.xpath('//div[@class="bookname"]/h1/text()')[0]
    detailTextList = detailTextIng.xpath('//div[@id="content"]//text()')
    detailText = ''.join(detailTextList)
    with open(yourDir+'\\'+name+'\\'+str(i)+'.txt', 'w', encoding='utf-8') as fp:
        fp.write(detailTitle+'\n'+detailText+'\n\n\n\n')


def txtCollect(name,m,yourDir):
    if not os.path.isdir(yourDir+'\\小说'):
        os.makedirs(yourDir+'\\小说')
        eachPageText = open(yourDir + '\\' + name + '\\' + str(m) + '.txt', 'r', encoding='utf-8').read()
        with open(yourDir + '\\小说\\' + name + '.txt', 'a', encoding='utf-8') as fp:
            fp.write(eachPageText)
        time.sleep(0.001)
    else:
        eachPageText = open(yourDir+'\\'+name+'\\'+str(m)+'.txt', 'r', encoding='utf-8').read()
        with open(yourDir+'\\小说\\'+name+'.txt', 'a', encoding='utf-8') as fp:
            fp.write(eachPageText)
        # time.sleep(0.001)


def guoLv():
    with open() as fp:
        page = fp.read()
        chancePage = 



url = 'https://www.xbiquge.la/89/89330/'
yourDir = 'D:\\ceshi'
zhang = getUrl(url)
name = findTitle(url, zhang, yourDir)
zhangList = findZhang(zhang)
GenXin,Shu = isGenXin(yourDir,name,zhangList)
Shu = Shu-1
Shu2 = Shu+1
sum = 0
startTime = time.time()
# sys.exit()
for i in range(len(GenXin)):
    Shu = Shu+1
    t1 = threading.Thread(target=findText,args=[GenXin[i], Shu, name, yourDir])
    t1.start()
    sum = sum+1
    baiFenBi = sum/len(GenXin)*100
    s = '\r已完成%d' % baiFenBi + '%'
    print(s.ljust(3), end='', flush=True)
    time.sleep(0.01)
t1.join()
time.sleep(8)
endTime = time.time()
print('\n下载共使用了'+str(endTime-startTime)+'秒\n现在开始处理文件...')
for m in range(Shu2,len(zhangList)):
    print(str(m))
    txtCollect(name,m,yourDir)
    time.sleep(0.1)
#shutil.rmtree(yourDir+'\\'+name)
print('处理完成')
sys.exit()


