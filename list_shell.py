Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [1,2,3,4,5,5,12,2,4,7,'python','hi',23.44,45.64]
>>> x[0]
1
>>> x[4]
5
>>> x[0:5]
[1, 2, 3, 4, 5]
>>> x[0:10:2]
[1, 3, 5, 12, 4]
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> data = []
>>> data.append(45)
>>> data
[45]
>>> data.append(4)
>>> data.append(12)
>>> data.append(3)
>>> data.append(19)
>>> data.append(30)
>>> data
[45, 4, 12, 3, 19, 30]
>>> import sys
>>> sys.getsizeof(list())
56
>>> sys.getsizeof([])
56
>>> sys.getsizeof([5])
64
>>> sys.getsizeof([5,7])
72
>>> sys.getsizeof([5,7,'h'])
120
>>> 120 - 72
48
>>> sys.getsizeof([5,7,'he'])
120
>>> sys.getsizeof([5,7,'hello'])
120
>>> sys.getsizeof([5,7,'hello world'])
120
>>> sys.getsizeof([5,7,'hello world','b'])
120
>>> sys.getsizeof([5,7,'hello world','bye'])
120
>>> sys.getsizeof([5,7,'hello world','bye world'])
120
>>> sys.getsizeof([5,7,'hello world','bye world','h','i'])
152
>>> sys.getsizeof([5,7,'hello world','bye world','h'])
120
>>> sys.getsizeof([5000,7000,'hello world','bye world','h'])
120
>>> data
[45, 4, 12, 3, 19, 30]
>>> data.append(3,4,5,5,2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    data.append(3,4,5,5,2)
TypeError: list.append() takes exactly one argument (5 given)
>>> data.extend([3,4,4,54,6,8,8])
>>> data
[45, 4, 12, 3, 19, 30, 3, 4, 4, 54, 6, 8, 8]
>>> data.append([3,4,5,5,2])
>>> data
[45, 4, 12, 3, 19, 30, 3, 4, 4, 54, 6, 8, 8, [3, 4, 5, 5, 2]]
>>> data.insert(2,100)
>>> data
[45, 4, 100, 12, 3, 19, 30, 3, 4, 4, 54, 6, 8, 8, [3, 4, 5, 5, 2]]
>>> data.pop()
[3, 4, 5, 5, 2]
>>> data
[45, 4, 100, 12, 3, 19, 30, 3, 4, 4, 54, 6, 8, 8]
>>> data.pop(4)
3
>>> data
[45, 4, 100, 12, 19, 30, 3, 4, 4, 54, 6, 8, 8]
>>> data.remove(4)
>>> data
[45, 100, 12, 19, 30, 3, 4, 4, 54, 6, 8, 8]
>>> data.count(4)
2
>>> data.reverse()
>>> data
[8, 8, 6, 54, 4, 4, 3, 30, 19, 12, 100, 45]
>>> data.sort()
>>> data
[3, 4, 4, 6, 8, 8, 12, 19, 30, 45, 54, 100]
>>> data.sort(reverse=True)
>>> data
[100, 54, 45, 30, 19, 12, 8, 8, 6, 4, 4, 3]
>>> data = []
>>> for i in range(1,21):
	if i % 2 == 0:
		data.append(i)

		
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> data = [i for i in range(1,21)]
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> data = [i for i in range(1,21) if i % 2 == 0]
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> data = [[i,j] for  i in range(10)  for j in range(10) if i != j]
>>> data
[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 0], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [3, 0], [3, 1], [3, 2], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [4, 0], [4, 1], [4, 2], [4, 3], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 6], [5, 7], [5, 8], [5, 9], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 7], [6, 8], [6, 9], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 8], [7, 9], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 9], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8]]
>>> data = [3,2,5,7,8,5]
>>> data_1 = data
>>> data
[3, 2, 5, 7, 8, 5]
>>> data_1
[3, 2, 5, 7, 8, 5]
>>> data is data_1
True
>>> data[0] = 100
>>> data
[100, 2, 5, 7, 8, 5]
>>> data_1
[100, 2, 5, 7, 8, 5]
>>> data_2 = data[:]
>>> data == data_2
True
>>> data is data_2
False
>>> data
[100, 2, 5, 7, 8, 5]
>>> data_2
[100, 2, 5, 7, 8, 5]
>>> data_2[0] = 10
>>> data_2
[10, 2, 5, 7, 8, 5]
>>> data
[100, 2, 5, 7, 8, 5]
>>> data = [4,3,3,6,[1,2,3,6,],4,5,6,5,7,6]
>>> data_2 = data.copy()
>>> data is data_2
False
>>> data_2[0]= 100
>>> data_2
[100, 3, 3, 6, [1, 2, 3, 6], 4, 5, 6, 5, 7, 6]
>>> data
[4, 3, 3, 6, [1, 2, 3, 6], 4, 5, 6, 5, 7, 6]
>>> data[4]
[1, 2, 3, 6]
>>> data[4][0]
1
>>> data[4][0] = 100
>>> data
[4, 3, 3, 6, [100, 2, 3, 6], 4, 5, 6, 5, 7, 6]
>>> data_2
[100, 3, 3, 6, [100, 2, 3, 6], 4, 5, 6, 5, 7, 6]
>>> 