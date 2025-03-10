# >>> import numpy as np
# >>> l = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24\]]]
# >>> a = np.array(1)
# >>> a
# array(1)
# >>> a = np.array(l)
# >>> a
# array([[[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]],

#        [[13, 14, 15, 16],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24]]])
# >>> a[:,:,0:1]
# array([[[ 1],
#         [ 5],
#         [ 9]],

#        [[13],
# >>> a = np.arange(1,25).reshape(2,3,4)
# >>> a
# array([[[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]],

#        [[13, 14, 15, 16],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24]]])
# >>> a[[0,1],[1,1],[2,1]]
# array([ 7, 18])
# >>> a = np.array([10,20,30,40])
# >>> boolean_array = np.array([True,False,False,True])
# >>> b_a = a>25
# >>> a[b_a]
# array([30, 40])
# >>> a = np.array([10,-5,20,40,-3,-1,75])
# >>> a
# array([10, -5, 20, 40, -3, -1, 75])
# >>> a[a < 0]
# array([-5, -3, -1])
# >>> a[a > 0]
# array([10, 20, 40, 75])
# >>> a[a%2 == 0]
# array([10, 20, 40])
# >>> a = np.arange(10,101,10)
# >>> a
# array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
# >>> b = a[[0,2,5]]
# >>> b
# array([10, 30, 60])
# >>> a[0] = 333
# >>> a
# array([333,  20,  30,  40,  50,  60,  70,  80,  90, 100])
# >>> a = np.arange(10,51,10)
# >>> a
# array([10, 20, 30, 40, 50])
# >>> for x in np.nditer(a):
# ...         print(x)
# ...         
# 10
# 20
# 30
# 40
# 50
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for x in np.nditer(a):
# ...             print(x)
# ... 
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# >>> a = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
# >>> for x in np.nditer(a):
# ...                 print(x)
# ... 
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for x in np.nditer(a[:,:2]):
# ...                     print(x)
# ... 
# 10
# 20
# 40
# 50
# 70
# 80
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for x in np.nditer(a,flags=['buffered'],op_dtypes=['float']):
# ...                         print(x)
# ...                         print(a)
# ... 
# 10.0
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# 20.0
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# 30.0
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# >>> import numpy as np
# >>> a = np.array([10,20,30,40,50])
# >>> for pos,element in np.ndenumerate(a):
# ...                             print(f'{element} element present at index/position:{\pos}')
# ... 
# 10 element present at index/position:(0,)
# 20 element present at index/position:(1,)
# 30 element present at index/position:(2,)
# 40 element present at index/position:(3,)
# 50 element present at index/position:(4,)
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for pos,element in np.ndenumerate(a):
# ...                                 print(f'{element} element present at index/positi\on:{pos}')
# ... 
# 10 element present at index/position:(0, 0)
# 20 element present at index/position:(0, 1)
# 30 element present at index/position:(0, 2)
# 40 element present at index/position:(1, 0)
# 50 element present at index/position:(1, 1)
# 60 element present at index/position:(1, 2)
# 70 element present at index/position:(2, 0)
# 80 element present at index/position:(2, 1)
# 90 element present at index/position:(2, 2)
# >>> a = np.arange(1,25).reshape(2,3,4)
# >>> for pos,element in np.ndenumerate(a):
# ...                                     print(f'{element} element present at index/po\sition:{pos}')
# ... 
# 1 element present at index/position:(0, 0, 0)
# 2 element present at index/position:(0, 0, 1)
# 3 element present at index/position:(0, 0, 2)
# 4 element present at index/position:(0, 0, 3)
# 5 element present at index/position:(0, 1, 0)
# 6 element present at index/position:(0, 1, 1)
# 7 element present at index/position:(0, 1, 2)
# 8 element present at index/position:(0, 1, 3)
# 9 element present at index/position:(0, 2, 0)
# 10 element present at index/position:(0, 2, 1)
# 11 element present at index/position:(0, 2, 2)
# 12 element present at index/position:(0, 2, 3)
# 13 element present at index/position:(1, 0, 0)
# 14 element present at index/position:(1, 0, 1)
# 15 element present at index/position:(1, 0, 2)
# 16 element present at index/position:(1, 0, 3)
# 17 element present at index/position:(1, 1, 0)
# 18 element present at index/position:(1, 1, 1)
# 19 element present at index/position:(1, 1, 2)
# 20 element present at index/position:(1, 1, 3)
# 21 element present at index/position:(1, 2, 0)
# 22 element present at index/position:(1, 2, 1)
# 23 element present at index/position:(1, 2, 2)
# 24 element present at index/position:(1, 2, 3)
# >>> a = np.array([10,20,30,40])
# >>> a
# array([10, 20, 30, 40])
# >>> a.2
#   File "<python-input-80>", line 1
#     a.2
#      ^^
# SyntaxError: invalid syntax
# >>> a+2
# array([12, 22, 32, 42])
# >>> a-2
# array([ 8, 18, 28, 38])
# >>> a*2
# array([20, 40, 60, 80])
# >>> a%2
# array([0, 0, 0, 0])
# >>> a/2
# array([ 5., 10., 15., 20.])
# >>> a//2
# array([ 5, 10, 15, 20])
# >>> a = np.array([[10,20,30],[40,50,60]])
# >>> a
# array([[10, 20, 30],
#        [40, 50, 60]])
# >>> a+2
# array([[12, 22, 32],
#        [42, 52, 62]])
# >>> a-2
# array([[ 8, 18, 28],
#        [38, 48, 58]])
# >>> a*2
# array([[ 20,  40,  60],
#        [ 80, 100, 120]])
# >>> a**2
# array([[ 100,  400,  900],
#        [1600, 2500, 3600]])
# >>> a/2
# array([[ 5., 10., 15.],
#        [20., 25., 30.]])
# >>> a//
#   File "<python-input-94>", line 1
#     a//
#        ^
# SyntaxError: invalid syntax
# >>> a//2
# array([[ 5, 10, 15],
#        [20, 25, 30]])
# >>> a = np.arange(6)
# >>> a
# array([0, 1, 2, 3, 4, 5])
# >>> a/0
# <python-input-98>:1: RuntimeWarning: divide by zero encountered in divide
#   a/0
# <python-input-98>:1: RuntimeWarning: invalid value encountered in divide
#   a/0
# array([nan, inf, inf, inf, inf, inf])
# >>> 
# >>> import numpy as np
# >>> l = [[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24\]]]
# >>> a = np.array(1)
# >>> a
# array(1)
# >>> a = np.array(l)
# >>> a
# array([[[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]],

#        [[13, 14, 15, 16],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24]]])
# >>> a[:,:,0:1]
# array([[[ 1],
#         [ 5],
#         [ 9]],

#        [[13],
# >>> a = np.arange(1,25).reshape(2,3,4)
# >>> a
# array([[[ 1,  2,  3,  4],
#         [ 5,  6,  7,  8],
#         [ 9, 10, 11, 12]],

#        [[13, 14, 15, 16],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24]]])
# >>> a[[0,1],[1,1],[2,1]]
# array([ 7, 18])
# >>> a = np.array([10,20,30,40])
# >>> boolean_array = np.array([True,False,False,True])
# >>> b_a = a>25
# >>> a[b_a]
# array([30, 40])
# >>> a = np.array([10,-5,20,40,-3,-1,75])
# >>> a
# array([10, -5, 20, 40, -3, -1, 75])
# >>> a[a < 0]
# array([-5, -3, -1])
# >>> a[a > 0]
# array([10, 20, 40, 75])
# >>> a[a%2 == 0]
# array([10, 20, 40])
# >>> a = np.arange(10,101,10)
# >>> a
# array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
# >>> b = a[[0,2,5]]
# >>> b
# array([10, 30, 60])
# >>> a[0] = 333
# >>> a
# array([333,  20,  30,  40,  50,  60,  70,  80,  90, 100])
# >>> a = np.arange(10,51,10)
# >>> a
# array([10, 20, 30, 40, 50])
# >>> for x in np.nditer(a):
# ...         print(x)
# ...         
# 10
# 20
# 30
# 40
# 50
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for x in np.nditer(a):
# ...             print(x)
# ... 
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# >>> a = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
# >>> for x in np.nditer(a):
# ...                 print(x)
# ... 
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for x in np.nditer(a[:,:2]):
# ...                     print(x)
# ... 
# 10
# 20
# 40
# 50
# 70
# 80
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for x in np.nditer(a,flags=['buffered'],op_dtypes=['float']):
# ...                         print(x)
# ...                         print(a)
# ... 
# 10.0
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# 20.0
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# 30.0
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# >>> import numpy as np
# >>> a = np.array([10,20,30,40,50])
# >>> for pos,element in np.ndenumerate(a):
# ...                             print(f'{element} element present at index/position:{\pos}')
# ... 
# 10 element present at index/position:(0,)
# 20 element present at index/position:(1,)
# 30 element present at index/position:(2,)
# 40 element present at index/position:(3,)
# 50 element present at index/position:(4,)
# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> for pos,element in np.ndenumerate(a):
# ...                                 print(f'{element} element present at index/positi\on:{pos}')
# ... 
# 10 element present at index/position:(0, 0)
# 20 element present at index/position:(0, 1)
# 30 element present at index/position:(0, 2)
# 40 element present at index/position:(1, 0)
# 50 element present at index/position:(1, 1)
# 60 element present at index/position:(1, 2)
# 70 element present at index/position:(2, 0)
# 80 element present at index/position:(2, 1)
# 90 element present at index/position:(2, 2)
# >>> a = np.arange(1,25).reshape(2,3,4)
# >>> for pos,element in np.ndenumerate(a):
# ...                                     print(f'{element} element present at index/po\sition:{pos}')
# ... 
# 1 element present at index/position:(0, 0, 0)
# 2 element present at index/position:(0, 0, 1)
# 3 element present at index/position:(0, 0, 2)
# 4 element present at index/position:(0, 0, 3)
# 5 element present at index/position:(0, 1, 0)
# 6 element present at index/position:(0, 1, 1)
# 7 element present at index/position:(0, 1, 2)
# 8 element present at index/position:(0, 1, 3)
# 9 element present at index/position:(0, 2, 0)
# 10 element present at index/position:(0, 2, 1)
# 11 element present at index/position:(0, 2, 2)
# 12 element present at index/position:(0, 2, 3)
# 13 element present at index/position:(1, 0, 0)
# 14 element present at index/position:(1, 0, 1)
# 15 element present at index/position:(1, 0, 2)
# 16 element present at index/position:(1, 0, 3)
# 17 element present at index/position:(1, 1, 0)
# 18 element present at index/position:(1, 1, 1)
# 19 element present at index/position:(1, 1, 2)
# 20 element present at index/position:(1, 1, 3)
# 21 element present at index/position:(1, 2, 0)
# 22 element present at index/position:(1, 2, 1)
# 23 element present at index/position:(1, 2, 2)
# 24 element present at index/position:(1, 2, 3)
# >>> a = np.array([10,20,30,40])
# >>> a
# array([10, 20, 30, 40])
# >>> a.2
#   File "<python-input-80>", line 1
#     a.2
#      ^^
# SyntaxError: invalid syntax
# >>> a+2
# array([12, 22, 32, 42])
# >>> a-2
# array([ 8, 18, 28, 38])
# >>> a*2
# array([20, 40, 60, 80])
# >>> a%2
# array([0, 0, 0, 0])
# >>> a/2
# array([ 5., 10., 15., 20.])
# >>> a//2
# array([ 5, 10, 15, 20])
# >>> a = np.array([[10,20,30],[40,50,60]])
# >>> a
# array([[10, 20, 30],
#        [40, 50, 60]])
# >>> a+2
# array([[12, 22, 32],
#        [42, 52, 62]])
# >>> a-2
# array([[ 8, 18, 28],
#        [38, 48, 58]])
# >>> a*2
# array([[ 20,  40,  60],
# >>> a = np.array([1,2,3,4])
# >>> b = np.array([10,20,30,40])
# >>> a.ndim
# 1
# >>> b.ndim
# 1
# >>> a.shape
# (4,)
# >>> b.shape
# (4,)
# >>> a.size
# 4
# >>> b.size
# 4
# >>> a+b
# array([11, 22, 33, 44])
# >>> a-b
# array([ -9, -18, -27, -36])
# >>> a*b
# array([ 10,  40,  90, 160])
# >>> a**b
# array([              1,         1048576, 205891132094649,               0])
# >>> b/a
# array([10., 10., 10., 10.])
# >>> b//a
# array([10, 10, 10, 10])
# >>> a = np.array([[1,2],[3,4]])
# >>> b = np.array([[5,6],[7,8]])
# >>> a+b
# array([[ 6,  8],
#        [10, 12]])
# >>> a-b
# array([[-4, -4],
#        [-4, -4]])
# >>> a*b
# array([[ 5, 12],
#        [21, 32]])
# >>> a/b
# array([[0.2       , 0.33333333],
#        [0.42857143, 0.5       ]])
# >>> a//b
# array([[0, 0],
#        [0, 0]])
# >>> b//a
# array([[5, 3],
#        [2, 2]])
# >>> a = np.array([10,20,30])
# >>> b = np.array([10,20,30,40])
# >>> a+b
# Traceback (most recent call last):
#   File "<python-input-123>", line 1, in <module>
#     a+b
#     ~^~
# ValueError: operands could not be broadcast together with shapes (3,) (4,)
# >>> a = np.array([10,20,30])
# >>> b = np.array([1,2,3])
# >>> np.add(a,b)
# array([11, 22, 33])
# >>> np.subtract(a,b)
# array([ 9, 18, 27])
# >>> np.multiply(a,b)
# array([10, 40, 90])
# >>> np.divide(a,b)
# array([10., 10., 10.])
# >>> np.floor_divide(a,b)
# array([10, 10, 10])
# >>> np.mod(a,b)
# array([0, 0, 0])
# >>> np.power(a,b)
# array([   10,   400, 27000])
# >>> a = np.array([10,20,30])
# >>> b = np.array([40])
# >>> a+b
# array([50, 60, 70])
# >>> a = np.array([[10,20],[30,40],[50,60]])
# >>> b = np.array([10,20])   
# >>> a+b
# array([[20, 40],
#        [40, 60],
#        [60, 80]])
# >>> a = np.array([[10],[20],[30]])
# >>> b = np.array([10,20,30])
# >>> a+b
# array([[20, 30, 40],
#        [30, 40, 50],
#        [40, 50, 60]])
# >>> 