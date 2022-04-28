import numpy as np
# 操作数组
# 不用编写循环即可对数据执行批量运算，这就是Numpy数组运算特点，Numpy称为矢量化
# 大小相同的数组之间的任何算术运算都可以用Numpy实现

# 1.加法运算
n1 = np.array([2,3])
n2 = np.array([4,5])
n3 = n1+n2
print(n3)

# 2.减法和乘除法运算
n4 = n1-n2
n5 = n1*n2
n6 = n1/n2
print(n4,'\n',n5,'\n',n6)

# 3.幂运算
# 幂是数组中对应位置元素的幂运算，使用‘**’运算符进行运算
n7 = n1**n2
print(n7)


# 比较运算
# Numpy创建的数组可以使用逻辑运算符进行比较运算
# 运算结果是布尔值数组，数组中的布尔值为相比较的数组在相同位置元素的比较结果
n1 = np.array([2,3,9,45])
n2 = np.array([4,5,9,11])
print(n1>=n2)
print(n1<=n2)
print(n1==n2)
print(n1!=n2)


# 复制数组
n8 = n1.copy()
print(n8)

# 数组的索引和切片
# [start:stop:step]（列表一样）
print(n1[:3])

# 二维数组索引
# 二维数组索引可以使用array[n,m]的方式，以逗号分隔，表示第n个数组的第m个元素
n1 = np.array([[2,3,4],[5,6,7]])
print(n1)
# 第一组
print(n1[0])
# 第一组，第二个
print(n1[0,1])


# 二维数组的切片式索引
n1 = np.array([[2,3,4],[5,6,7],[8,9,10]])
# 前两组，前两位
print(n1[:2,:2])
# 后两组，后两位
print(n1[1:,1:])


# 数组拼接
n1 = np.array([1,2,3])
n2 = np.array([4,5,6])
# 水平拼接
n3 = np.hstack((n1,n2))
# 竖直拼接
n4 = np.vstack((n1,n2))

print(n3)
print(n4)






