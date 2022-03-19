import threading
import time

print('start the project')
def takeANap():
    time.sleep(5)
    print('Wake up!')
#target=函数名！！！！！不是调用函数！！！！！
threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('end the project')

#向线程的目标函数传递参数
# def MySnow(me,wife,son):
#     time.sleep(2)
#     print('%s love %s,and we have a son,his name is %s' %(me,wife,son))
#
# print('this is my family')
# threadObj = threading.Thread(target=MySnow, args=['李杨明','张小雪','李梦雪'])
# threadObj.start()
#
# print('i will love my family in my life')



