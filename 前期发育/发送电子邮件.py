# 正如http是计算机用来通过因特网发送网页的协议，
# 简单邮件传输协议（SMTP）是用于发送电子邮件的协议。
# SMTP只负责向别人发送邮件，另外一个协议，IMAP负责取回发送给你的邮件
import smtplib
#不要开ml！！！不要开代理！！！！
#原因是开了百度直联

# 连接到SMTP服务器
smtpObj = smtplib.SMTP(host='smtp.163.com',port=25)
# 向服务器打招呼
smtpObj.ehlo()
# 开始TLS加密，连接加密
smtpObj.starttls()
#登录邮箱
smtpObj.login('lym104432061@163.com', 'SSEBGRLHKTFROBHU')
# msg.as_string()：为一个字符串类型 ，as_string()是将发送的信息msg变为字符串类型。
text = 'Subject:\n  Hello,zhangxiaoxue,my wife!!!'
# sendmail() 发送者，接受者，正文字符串    必须加  Subject:\n 开头，作为邮箱的主题行
smtpObj.sendmail(from_addr='lym104432061@163.com',to_addrs='486381511@qq.com', msg=text)
# 从SMTP服务器断开
smtpObj.quit()

