Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello World, This is Python programming"
>>> len(text)
39
>>> text[50]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    text[50]
IndexError: string index out of range
>>> text[38]
'g'
>>> text[0]
'H'
>>> text[0:20]
'Hello World, This is'
>>> text[20:22]
' P'
>>> text[0,5]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    text[0,5]
TypeError: string indices must be integers
>>> text[:]
'Hello World, This is Python programming'
>>> text[10:]
'd, This is Python programming'
>>> text[:20]
'Hello World, This is'
>>> text[0:100]
'Hello World, This is Python programming'
>>> text[10:0]
''
>>> text[10:0:-1]
'dlroW olle'
>>> text[10:1:-1]
'dlroW oll'
>>> text[0:10]
'Hello Worl'
>>> text[10::-1]
'dlroW olleH'
>>> text[6:6+5]
'World'
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text[-1:-3:-1]
'gn'
>>> text[::-1]
'gnimmargorp nohtyP si sihT ,dlroW olleH'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.swapcase()
'hELLO wORLD, tHIS IS pYTHON PROGRAMMING'
>>> text.replace(text[0:10], text[0:10].upper())
'HELLO WORLd, This is Python programming'
>>> text.replace('o','x')
'Hellx Wxrld, This is Pythxn prxgramming'
>>> text.replace('o','x',2)
'Hellx Wxrld, This is Python programming'
>>> text.replace('o','x',-2)
'Hellx Wxrld, This is Pythxn prxgramming'
>>> text.find('this')
-1
>>> text.find('This')
13
>>> text.index('o')
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.find('o')
4
>>> text.find('o')
4
>>> text.count('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.find('o',26)
30
>>> count = text.count('o')
>>> count
4
>>> x = 0
>>> for i in range(count):
	index = text.find('o', x)
	x = index + 1

	
>>> 4
4
>>> x = 0
>>> for i in range(count):
	index = text.find('o', x)
	print(index)
	x = index + 1

	
4
7
25
30
>>> for i in range(len(text)):
	print(i, text[i])

	
0 H
1 e
2 l
3 l
4 o
5  
6 W
7 o
8 r
9 l
10 d
11 ,
12  
13 T
14 h
15 i
16 s
17  
18 i
19 s
20  
21 P
22 y
23 t
24 h
25 o
26 n
27  
28 p
29 r
30 o
31 g
32 r
33 a
34 m
35 m
36 i
37 n
38 g
>>> text.count('x')
0
>>> text.split()
['Hello', 'World,', 'This', 'is', 'Python', 'programming']
>>> text.split(",")
['Hello World', ' This is Python programming']
>>> text = "    hello    "
>>> text.strip()
'hello'
>>> text.lstrip()
'hello    '
>>> text.rstrip()
'    hello'
>>> text.strip()
'hello'
>>> text
'    hello    '
>>> text = text.strip()
>>> text
'hello'
>>> text.encode()
b'hello'
>>> text.startswith('H')
False
>>> text.startswith('h')
True
>>> text.startswith('w')
False
>>> text.startswith('w',5)
False
>>> text.startswith('w',6)
False
>>> text.startswith('w',4)
False
>>> text
'hello'
>>> text = "hello world"
>>> text.startswith('w',5)
False
>>> text.startswith('w',4)
False
>>> text[5]
' '
>>> text.startswith('w',6)
True
>>> text.endswith('?')
False
>>> text.isalnum()
False
>>> text.isdigit()
False
>>> text.islower()
True
>>> text.isupper()
False
>>> 