class ClassA(object):
    My_wife = '雪'
    def method(self):
        print('我是父类')

class ClassB(ClassA):
    def method(self):
        print('我是子类')

#子类中重新定义了一个method方法覆盖了原来父类的method方法

obj = ClassB()
print(ClassB.My_wife)
obj.method()


#类的多态
#多态指对不同类型的变量进行相同的操作，它会根据对象（或类）的不同做出不同的行为
# 1+1=2
# a+b=ab

class User(object):
    #父类
    def __init__(self,name):
        self.name = name
    #这里是用于后面的子类重写类的方法
    def printUser(self):
        print('Hello!'+self.name)

class UserVip(User):
    #子类
    #重写类的方法
    def printUser(self):
        print('Hello! 尊敬的Vip用户：'+self.name)

class UserGeneral(User):
    #子类
    #也是重写类的方法，这样就有了两种不一样的结果
    def printUser(self):
        print('Hello! 尊敬的用户：'+self.name)

#用于调用不同对象的方法
def printUserInfo(user):
    user.printUser()

#实例化UserVip对象
useVip = UserVip('宁长久')
#调用对象的方法
printUserInfo(useVip)
#实例化UserGeneral对象
userGeneral = UserGeneral('陆嫁嫁')
#调用类的方法
printUserInfo(userGeneral)

#不同的对象，产生了不一样的结果