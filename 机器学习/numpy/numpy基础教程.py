import numpy
import numpy as np

# 数组的类型
print(np.int8(3.1415))
print(np.float64(8))
print(np.float64(True))


# 创建数组
# array方法   np.array(object,dtype,copy,order,subok,ndmin)
# object：任何具有数组接口方法的对象
# dtype：数据类型
# copy：可选参数，布尔型，默认数值为True，则object对象被复制
# ndmin：指定生成数组的最小维数
# order：“元素在内存中的出现顺序，其值为K、A、C、F。
# 如果object参数不是数组，则新创建的数组将按行排列（C），
# 如果值为F，则按列排列；
# 如果object参数是一个数组，则以下顺序成立：C（按行）、F（按列）、A（原顺序）、K（元素在内存中的出现顺序）”

# 一维数组二维数组
n1 = np.array([1,2,3])
n2 = np.array([0.1,0.2,0.3])
n3 = np.array([[1,2],[3,4]])
print(n1)
print(n2)
print(n3)



# 创建浮点类型数组
list = [1,2,3]
n4 = np.array(object=list,dtype=float)
print(n4)

# 创建三维数组
n5 = np.array(object=list,ndmin=3)
print(n5)


# 创建指定维度和数据类型未初始化的数组
# 创建指定维度和数据类型未初始化的数组主要使用empty()方法，
# 数组元素因为未被初始化会自动取随机值。
# 如果要改变数组类型，可以使用dtype参数，如将数组类型设为整型，dtype=int。
n6 = np.empty([2,3],dtype=int)
# 两行三列数组
print(n6)

# 使用0来填充数组
# 三行三列由0来填充的数组
n7 = np.zeros([3,3],dtype=int)
print(n7)

# 使用1来填充数组
# 三行四列由1来填充的数组
n8 = np.ones([3,4])
print(n8)

# 创建随机数组
# np.random.randint(low,hight,size)
# low：下限，hight：上限，size：维数
# 生成1个数组，里面有6个元素，元素是1到10随机取值
n9 = np.random.randint(1,10,6)
print(n9)
# 指定维数
n10 = np.random.randint(1,10,size=[2,5])
print(n10)











