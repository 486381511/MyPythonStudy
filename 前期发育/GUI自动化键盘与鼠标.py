#图形用户界面自动化（大杀招）GUI自动化
import pyautogui
import time

# 暂停和自动防故障装置
# 1.payautogui.PAUSE = 1.5   每次调用pyautogui函数都有1.5秒的停顿
# 2.鼠标放到屏幕左上角，可以关 pyautogui.FAILSAFE = False

# pyautogui鼠标函数使用x，y坐标，原点xy为0，都是正，没有负数

# 获取屏幕坐标
# size()返回一个元组，包含屏幕的宽高的像素值
pyautogui.size()

#移动鼠标
# 绝对位置
# moveTo()有两个参数 1.指定位置  2.移动过程的时间 duration关键字
pyautogui.moveTo((1000,1000),duration=0.6)

# 相对位置,以鼠标当前位置为原点
# moveRel()接受2个参数 1.相对位置移动参数  2.移动过程的时间 duration关键字
pyautogui.moveRel((500,-300),duration=0.9)

# 获取鼠标位置
pyautogui.position()


# 鼠标交互
# 点击鼠标
# click()传入两个参数
# 1.xy位置
# 2.指定鼠标按键 button，值分别为'left','middle','right'
pyautogui.click(1000,1000) #不写button，默认就是左键
# click实际是封装了pyautogui.mouseDown()与pyautogui.mouseUp()
#pyautogui.mouseDown()是按下鼠标
#pyautogui.mouseUp()是释放鼠标
pyautogui.mouseDown(1000,1000)
time.sleep(2)
pyautogui.mouseUp(1000,1000)
#还有其他doubleClick双击左键  rightClick双击右键  middleClick双击中键


#拖动鼠标，拖动意味着移动鼠标，同时按住按钮不放，用法与前面一样
pyautogui.dragTo((100,500),duration=2)
pyautogui.dragRel((200,900),duration=2)


#滚动鼠标
#scroll(),传入一个整型参数，说明向上或向下滚动多少单位,正数向上，负数向下
pyautogui.scroll(200)


#获取屏幕快照
im = pyautogui.screenshot()
#im变量将包含一个屏幕快照的Image对象，可以调用Pillow方法对该Image对象进行操作


#分析屏幕快照
#如果屏幕上指定的x和y坐标处的像素与指定的颜色匹配
#pyautogui的pixelMatchesColor()函数将返回True
#第一个参数是x和y的坐标,这次不能是元组了     第二个参数是指定的RGB颜色
print(pyautogui.pixelMatchesColor(1000,1000,(255,255,255)))



#图像识别
pyautogui.locateOnScreen('.\\学习资源\\猫猫.png')
#传入一个图片相对位置
#计算机判断屏幕当前有没有该图片的位置，有就返回一个四个整数元组
#(x,y,宽,高)，xy是该图像在屏幕上的左上角位置
#如果有多处就返回一个列表

#把该元组传给center函数，返回中心坐标位置
a = pyautogui.center((643,735,70,29))
pyautogui.click(a)





#控制键盘
#输入字符串
#typewrite有两个参数，一个是字符串，一个是输入每个字符的相隔时间，不写就秒输入
pyautogui.typewrite('Hello World',0.25)

#键名的列表
print(pyautogui.KEYBOARD_KEYS)

#按下和释放键盘
# pyautogui.keyDown()按 和pyautogui.Keyup释放
# 合并 pyautogui.press()



