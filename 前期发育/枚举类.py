from enum import Enum
Month = Enum('Moth',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sap','Oct','Nov','Dec'))
#Moth枚举名，后面的是枚举值
#遍历枚举类型
#
for name,member in Month.__members__.items():
    #获取Moth里边的成员
    print(name,'----------',member,'----------',member.value)

#直接引用一个常量
print('\n',Month.Jan)

#Enum定义了一个枚举类
#上面创建了一个有关月份的枚举类型Month，这里要注意构造参数‘
#第一个参数Month表示的是该枚举类的类名，第二个tuple参数，表示的是要枚举类的值
#当然，枚举类通过__members__遍历它的所有成员的方法
#member.value是自动赋值给成员的int类型的常量，默认是从1开始的。

#而且Enum的成员均为单例，并且不可实例化，不可更改
