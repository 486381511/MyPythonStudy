#popen中的P代表着process
#如果打开了一个应用程序的多个实例，每个实例都是一个程序的不同进程
#每个进程可以有多个线程，不像线程，进程无法直接读写类一个进程的变量
import subprocess
#属性看程序启动路径
#app = subprocess.Popen('D:\\CloudMusic\\cloudmusic.exe')
#向Popen()传递命令行参数
#向Popen中传一个列表，列表中第一个字符串是要启动的程序的文件名
#后续的字符串将是程序启动时，传递给该程序的命令行参数
#app = subprocess.Popen(['D:\\CloudMusic\\cloudmusic.exe','D:\\CloudMusic\\1n - デート2 (1n Cover).mp3'])


#在python中启动另外一个python脚本，就像启动其他程序一样
#向Popen()函数传一个列表，python程序与py文件
# open_python = subprocess.Popen(['D:\\python\\Scripts\\python.exe', 'C:\\Users\\yi\\PycharmProjects\\pythonProject\\多线程.py'])


#使用计算机系统默认程序打开相应的文件
file = subprocess.Popen(['start', 'D:\\ceshi\\005.jpg'], shell=True)
