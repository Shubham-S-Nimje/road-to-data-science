# >>> np.ones((2,3))
# array([[1., 1., 1.],
#        [1., 1., 1.]])
# >>> np.ones(10)
# array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
# >>> a = np.arange(1,21)
# >>> a
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
#        18, 19, 20])
# >>> a[a%2 == 0]
# array([ 2,  4,  6,  8, 10, 12, 14, 16, 18, 20])
# >>> a[a%6 == 0]
# array([ 6, 12, 18])
# >>> 

# >>> a = np.array([[1,1], [3,8]])
# >>> a
# array([[1, 1],
#        [3, 8]])
# >>> b = np.array([2200,10100])
# >>> b
# array([ 2200, 10100])
# >>> np.linalg.solve(a,b)
# array([1500.,  700.])
# >>> 
# >>> import array
# >>> a = array.array('i', [10,20,30])
# >>> a
# array('i', [10, 20, 30])
# >>> for x in a: 
# ...         print(x)
# ...         
# 10
# 20
# 30
# >>> l = [10,10.5,'Sunny',True]
# >>> l
# [10, 10.5, 'Sunny', True]
# >>> a = numpy.array(l)
# Traceback (most recent call last):
#   File "<python-input-105>", line 1, in <module>
#     a = numpy.array(l)
#         ^^^^^
# NameError: name 'numpy' is not defined
# >>> a = np.array(l)
# >>> a
# array(['10', '10.5', 'Sunny', 'True'], dtype='<U32')
# >>> 
# >>> l = [10,20,30,40]
# >>> a = np.array(l)
# >>> a
# array([10, 20, 30, 40])
# >>> l+2
# Traceback (most recent call last):
#   File "<python-input-114>", line 1, in <module>
#     l+2
#     ~^~
# TypeError: can only concatenate list (not "int") to list
# >>> a+2
# array([12, 22, 32, 42])
# >>> a/2
# array([ 5., 10., 15., 20.])
# >>> l*2
# [10, 20, 30, 40, 10, 20, 30, 40]
# >>> a*2
# array([20, 40, 60, 80])
# >>> 
# >>> l = [10,20,30,40]
# >>> a = np.array(l)
# >>> type(a)
# <class 'numpy.ndarray'>
# >>> a.ndim
# 1
# >>> a.dtype
# dtype('int64')
# >>> 

# >>> a = np.array([[10,20,30],[40,50,60],[70,80,90]])
# >>> a
# array([[10, 20, 30],
#        [40, 50, 60],
#        [70, 80, 90]])
# >>> a.shape
# (3, 3)
# >>> a.ndim
# 2
# >>> a.size
# 9
# >>> 
# >>> a = np.array([10,20,30.5],dtype=int)
# >>> a
# array([10, 20, 30])
# >>> a = np.array([10,20,30.5],dtype=bool)
# >>> a
# array([ True,  True,  True])
# >>> a = np.array([10,20,30.5],dtype=float)
# >>> a
# array([10. , 20. , 30.5])
# >>> a = np.array([10,20,30.5],dtype=complex)
# >>> a
# array([10. +0.j, 20. +0.j, 30.5+0.j])
# >>> a = np.array([10,'Sunny'],dtype=int)
# Traceback (most recent call last):
#   File "<python-input-137>", line 1, in <module>
#     a = np.array([10,'Sunny'],dtype=int)
# ValueError: invalid literal for int() with base 10: 'Sunny'
# >>> 