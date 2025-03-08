# import numpy as np
# PS D:\Learning\Learning Data Science\Road To Data Science> np.__version__
# np.__version__ : The term 'np.__version__' is not recognized as the name of a cmdlet, function, script 
# file, or operable program. Check the spelling of the name, or if a path was included, verify that the path 
# is correct and try again.
# At line:1 char:1
# + np.__version__
# + ~~~~~~~~~~~~~~
#     + CategoryInfo          : ObjectNotFound: (np.__version__:String) [], CommandNotFoundException
#     + FullyQualifiedErrorId : CommandNotFoundException
 
# PS D:\Learning\Learning Data Science\Road To Data Science> import numpy as np
# import : The term 'import' is not recognized as the name of a cmdlet, function, script file, or operable 
# program. Check the spelling of the name, or if a path was included, verify that the path is correct and try 
# again.
# At line:1 char:1
# + import numpy as np
# + ~~~~~~
#     + CategoryInfo          : ObjectNotFound: (import:String) [], CommandNotFoundException
#     + FullyQualifiedErrorId : CommandNotFoundException
 
# PS D:\Learning\Learning Data Science\Road To Data Science> py
# Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> np.__version__
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     np.__version__
#     ^^
# NameError: name 'np' is not defined
# >>> import numpy as np
# >>> np.__version__
# '2.2.3'
# >>> a=10
# >>> b=20
# >>> a+b
# 30
# >>> math.sqrt(4)
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     math.sqrt(4)
#     ^^^^
# NameError: name 'math' is not defined. Did you forget to import 'math'?
# >>> import math
# >>> math.sqrt(4)
# 2.0
# >>> a = np.zeros(10,10)
# Traceback (most recent call last):
#   File "<python-input-9>", line 1, in <module>
#     a = np.zeros(10,10)
# TypeError: Cannot interpret '10' as a data type
# >>> a = np.zeros((10,10))
# >>> a
# array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
# >>> type a)
#   File "<python-input-12>", line 1
#     type a)
#           ^
# SyntaxError: unmatched ')'
# >>> type a
#   File "<python-input-13>", line 1
#     type a
#           ^
# SyntaxError: invalid syntax
# >>> type(a)
# <class 'numpy.ndarray'>
# >>> a = np.zeros((10,10), dtype=int)
# >>> a
# array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
# >>> type(a)
# <class 'numpy.ndarray'>
# >>> np.arange((1,101))
# ... 
# ... 
# ... 
# KeyboardInterrupt
# >>> np.arange(1,101)
# array([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,
#         14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,
#         27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,
#         40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,
#         53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,  65,
#         66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,  78,
#         79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,
#         92,  93,  94,  95,  96,  97,  98,  99, 100])
# >>> a - np.identity(3)
# Traceback (most recent call last):
#   File "<python-input-19>", line 1, in <module>
#     a - np.identity(3)
#     ~~^~~~~~~~~~~~~~~~
# ValueError: operands could not be broadcast together with shapes (10,10) (3,3)
# >>> a = np.identity(3)
# >>> a
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])
# >>> a = np.identity(5)
# >>> a
# array([[1., 0., 0., 0., 0.],
#        [0., 1., 0., 0., 0.],
#        [0., 0., 1., 0., 0.],
#        [0., 0., 0., 1., 0.],
#        [0., 0., 0., 0., 1.]])
# >>> type(a)
# <class 'numpy.ndarray'>
# >>> 