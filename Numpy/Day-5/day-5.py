# >>> import sys
# >>> import numpy as np
# >>> a = np.array([10,20,30,40])
# >>> a
# array([10, 20, 30, 40])
# >>> print(sys.getsizeof(a))
# 144
# >>> a = np.array([10,20,30,40],dtype='int8')
# >>> a
# array([10, 20, 30, 40], dtype=int8)
# >>> print(sys.getsizeof(a))
# 116
# >>> b = a.astype('float64')
# >>> b
# array([10., 20., 30., 40.])
# >>> a.dtype
# dtype('int8')
# >>> b.dtype
# dtype('float64')
# >>> a = np.array([10,0,30,0])
# >>> x = np.bool(a)
# >>> a
# array([10,  0, 30,  0])
# >>> x
# array([ True, False,  True, False])
# >>> x = np.bool_(a)
# >>> x
# array([ True, False,  True, False])
# >>> a = np.array([10,20,30,40])
# >>> a
# array([10, 20, 30, 40])
# >>> a[0]
# np.int64(10)
# >>> a[-1]
# np.int64(40)
# >>> a[10]
# Traceback (most recent call last):
#   File "<python-input-244>", line 1, in <module>
#     a[10]
#     ~^^^^
# IndexError: index 10 is out of bounds for axis 0 with size 4
# >>> a = np.array([[10,20,30],[40,50,60]])
# >>> a
# array([[10, 20, 30],
#        [40, 50, 60]])
# >>> a[1][1]
# np.int64(50)
# >>> a[1][-2]
# np.int64(50)
# >>> a[-1][1]
# np.int64(50)
# >>> 

# >>> a = np.array([10,20,30,40])
# >>> a
# array([10, 20, 30, 40])
# >>> print(sys.getsizeof(a))
# 144
# >>> a = np.array([10,20,30,40],dtype='int8')
# >>> a
# array([10, 20, 30, 40], dtype=int8)
# >>> print(sys.getsizeof(a))
# 116
# >>> b = a.astype('float64')
# >>> b
# >>> a = np.arange(10,101,10)
# >>> a
# array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
# >>> a[2:5]
# array([30, 40, 50])
# >>> a[::1]
# array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
# >>> a[::-1]
# array([100,  90,  80,  70,  60,  50,  40,  30,  20,  10])
# >>> a[::-2]
# array([100,  80,  60,  40,  20])
# >>> a = np.array([[10,20],[30,40],[50,60]])
# >>> a
# array([[10, 20],
#        [30, 40],
#        [50, 60]])
# >>> a[0:1,:]
# array([[10, 20]])
# >>> a[0,:]
# array([10, 20])
# >>> a[0::2,:]
# array([[10, 20],
#        [50, 60]])
# >>> a[0:2,1:2]
# array([[20],
#        [40]])
# >>> a[:2,1:]
# array([[20],
#        [40]])
# >>> a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# >>> a
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12],
#        [13, 14, 15, 16]])
# >>> a[0:2,:]
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
# >>> a[0::3,:]
# array([[ 1,  2,  3,  4],
#        [13, 14, 15, 16]])
# >>> a[:,0:2]
# array([[ 1,  2],
#        [ 5,  6],
#        [ 9, 10],
#        [13, 14]])
# >>> a[:,::2]
# array([[ 1,  3],
#        [ 5,  7],
#        [ 9, 11],
#        [13, 15]])
# >>> a[1:3,1:3]
# array([[ 6,  7],
#        [10, 11]])
# >>> a[::3,::3]
# array([[ 1,  4],
#        [13, 16]])
# >>> 