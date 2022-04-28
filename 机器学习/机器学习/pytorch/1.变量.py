import torch

# pytorch中的数据都是封装成Tensor来引用的，Tensor实际上就类似于numpy中的数组
# 二者可以相互转换

# 生成一个(3,4)维度的数组
x = torch.Tensor(3,4)
print(x)
# 维数
print(x.ndim)
# shape形状与size()一样
print(x.shape)
print(x.size())
# 查看类型
print(x.dtype)
