---
layout: post
title: "图像处理笔记 -- NumPy 切片和索引"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility: hiddenz
mathjax: true
mermaid: truez
glslcanvas:
codeprint:
---


## NumPy 切片和索引

冒号分隔切片参数 start:stop:step 来进行切片操作：

```python
import numpy as np

a = np.arange(10)
b = a[2:7:2] # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)
```

```
[2  4  6]
```

切片还可以包括省略号 `…`，来使选择元组的长度与数组的维度相同。如果在行位置使用省略号，它将返回包含行中元素的 ndarray。

```python
import numpy as np

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a[...,1])   # 第 2 列元素
print (a[1,...])   # 第 2 行元素
print (a[...,1:])  # 第 2 列及剩下的所有元素
```

```
[2 4 5]
[3 4 5]
[[2 3]
 [4 5]
 [5 6]]
```

```python
>>> import numpy as np
>>> a = np.array([[[1,2],], [[3,4]]])
>>> a
array([[[1, 2]],
       [[3, 4]]])

>>> a[..., :1] # an index can only have a single ellipsis ('...')
array([[[1]],
       [[3]]])

>>> a[:, :, :1]
array([[[1]],
       [[3]]])
```


## NumPy 高级索引


### 整数数组索引

以下实例获取数组中 (0,0)，(1,1) 和 (2,0) 位置处的元素。

```python
import numpy as np

x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0,1,2],  [0,1,0]]
print (y)
```

```
[1  4  5]
```

以下实例获取了 4x3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。

```python
import numpy as np

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows, cols]
print ('这个数组的四个角元素是：')
print (y)
```

```
我们的数组是：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]

这个数组的四个角元素是：
[[ 0  2]
 [ 9 11]]
```

可以借助切片 `:` 或 `…` 与索引数组组合。如下面例子：

```python
import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = a[1:3, 1:3]
c = a[1:3, [1,2]]
d = a[..., 1:]
print(b)
print(c)
print(d)
```

```
[[5 6]
 [8 9]]

[[5 6]
 [8 9]]

[[2 3]
 [5 6]
 [8 9]]
```


### 布尔索引

我们可以通过一个布尔数组来索引目标数组。

布尔索引通过布尔运算（如：比较运算符）来获取符合指定条件的元素的数组。

以下实例获取大于 5 的元素：

```python
import numpy as np

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素
print ('大于 5 的元素是：')
print (x[x > 5])
```

```
我们的数组是：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]

大于 5 的元素是：
[ 6  7  8  9 10 11]
```

以下实例使用了 `~`（取补运算符）来过滤 NaN。

```python
import numpy as np

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print (a[~np.isnan(a)])
```

```
[1. 2. 3. 4. 5.]
```

以下实例演示如何从数组中过滤掉非复数元素。

```python
import numpy as np

a = np.array([1,  2+6j,  5,  3.5+5j])
print (a[np.iscomplex(a)])
```

```
[2.+6.j 3.5+5.j]
```


### 花式索引

花式索引指的是利用整数数组进行索引。

花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。对于使用一维整型数组作为索引，如果目标是一维数组，那么索引的结果就是对应位置的元素；如果目标是二维数组，那么就是对应下标的行。

花式索引跟切片不一样，它总是将数据复制到新数组中。

#### 传入顺序索引数组

```python
import numpy as np

x = np.arange(32).reshape((8,4))
print (x[[4,2,1,7]])
```

```
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19],
       [20, 21, 22, 23],
       [24, 25, 26, 27],
       [28, 29, 30, 31]])

[[16 17 18 19]
 [ 8  9 10 11]
 [ 4  5  6  7]
 [28 29 30 31]]
```

#### 传入倒序索引数组

```python
import numpy as np

x = np.arange(32).reshape((8,4))
print (x[[-4,-2,-1,-7]])
```

```
[[16 17 18 19]
 [24 25 26 27]
 [28 29 30 31]
 [ 4  5  6  7]]
```

#### 传入多个索引数组（要使用 np.ix_）

如果 np.xi_ 中输入两个列表，则第一个列表存的是待提取元素的行标，第二个列表存的是待提取元素的列标，第一个列表中的每个元素都会遍历第二个列表中的每个值，构成新矩阵的一行元素。

```python
import numpy as np

x = np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
```

```
x[1,0] x[1,3] x[1,1] x[1,2]
x[5,0] x[5,3] x[5,1] x[5,2]
x[7,0] x[7,3] x[7,1] x[7,2]
x[2,0] x[2,3] x[2,1] x[2,2]

[[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
```


### sample

掩码可以是任何与图像形状相同的布尔阵列（或可以广播到图像形状的形状）。

```python
nrows, ncols = camera.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows / 2, ncols / 2
outer_disk_mask = ((row - cnt_row)**2 + (col - cnt_col)**2 >
                   (nrows / 2)**2)
camera[outer_disk_mask] = 0
imgshow(camera)
```

{% include image.html url="/assets/images/201001-dip-numpy-slice/qdkztdoc06.png" %}

甚至可以进行布尔运算，可用于定义更复杂的掩码。

```python
lower_half = row > cnt_row
lower_half_disk = np.logical_and(lower_half, outer_disk_mask)
camera = data.camera()
camera[lower_half_disk] = 0
imgshow(camera)
```

{% include image.html url="/assets/images/201001-dip-numpy-slice/20201004180413.png" %}


## 向量和矩阵的点乘和叉乘


### 向量

点乘，也叫数量积。结果是一个向量在另一个向量方向上投影的长度，是一个标量。

叉乘，也叫向量积。结果是一个和已有两个向量都垂直的向量。

以我比较熟悉的图形学而言，一般点乘用来判断两个向量是否垂直，因为比较好算。也可以用来计算一个向量在某个方向上的投影长度，就像定义一样。

叉乘更多的是判断某个平面的方向。从这个平面上选两个不共线的向量，叉乘的结果就是这个平面的法向量。

两种不同的运算而已。

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([2, 2, 3])
np.dot(a, b)
np.cross(a, b)
a * b
np.multiply(a, b)
```

```
15 # dot
array([ 0,  3, -2]) # cross
array([2, 4, 9]) # *
array([2, 4, 9]) # multiply
```


### 矩阵

矩阵点乘：是矩阵各个对应元素相乘，这个时候要求两个矩阵必须同样大小。

矩阵叉乘：矩阵的乘法就是矩阵 a 的第 m 行乘以矩阵 b 的第 n 列，各个元素对应相乘然后求和作为第 m 行 n 列元素的值。

矩阵的点乘直接使用 \* 号即可，也可以使用 numpy 库的 multiply 函数，叉乘使用 dot 函数，这与向量相反。

```python
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
a * b
np.dot(a, b)
np.cross(a, b)
np.multiply(a, b)
```

```
array([[ 5, 12], # *
       [21, 32]])
array([[19, 22], # dot
       [43, 50]])
array([-4, -4]) # cross 不知道是个啥
array([[ 5, 12], # multiply
       [21, 32]])
```


### 比较

numpy 库的对象有数组和矩阵，两者看起来长得差不多，但在性质、运算上有很大不同。可通过 array 函数和 mat 函数相互转化。

向量：dot 是点乘法，cross 是叉乘，\* 和 multiply 为对于位置相乘。

矩阵：dot 是矩阵叉乘，\* 和 multiply 为对于位置相乘。

#### dot 函数

* 对于秩为 1 的数组，执行对应位置相乘，然后再相加，等价于向量的点乘；
* 对于秩不为 1 的二维数组，执行矩阵乘法运算，等价于矩阵的叉乘；

#### multiply 函数

* 数组和矩阵对应位置相乘，输出与相乘数组 / 矩阵的大小一致，效果上与运算符 \* 对数组效果一样。

#### 运算符 \* 号

* 对数组执行对应位置相乘，等价于 multiply 函数；
* 对矩阵执行对应位置相乘，等价于 multiply 函数。


## 参考

- [1] [NumPy 教程](https://www.runoob.com/numpy/numpy-tutorial.html)
- [2] [Python 之 Numpy 基础 {% include relref_zhihu.html %}](https://zhuanlan.zhihu.com/p/32242331)
- [3] <https://blog.csdn.net/wzyaiwl/article/details/106310705>

<hr class='reviewline'/>
<p class='reviewtip'>2021-01-23: review</p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.runoob.com/numpy/numpy-tutorial.html]({% include relref.html url="/backup/2020-10-01-dip-numpy-slice.md/www.runoob.com/c30f9bdf.html" %})
- [https://zhuanlan.zhihu.com/p/32242331]({% include relref.html url="/backup/2020-10-01-dip-numpy-slice.md/zhuanlan.zhihu.com/c493ef42.html" %})
- [https://blog.csdn.net/wzyaiwl/article/details/106310705]({% include relref.html url="/backup/2020-10-01-dip-numpy-slice.md/blog.csdn.net/4220be40.html" %})
