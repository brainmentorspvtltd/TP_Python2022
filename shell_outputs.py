Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 44
>>> y= 5
>>> a + y
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a + y
NameError: name 'a' is not defined
>>> x + y
49
>>> x - y
39
>>> x / y
8.8
>>> x * y
220
>>> x % y
4
>>> x / y
8.8
>>> x // y
8
>>> x ** y
164916224
>>> x ** 2
1936
>>> x ** 3
85184
>>> x ** 4
3748096
>>> x ** 5
164916224
>>> x > y
True
>>> x < y
False
>>> x = 6
>>> y = 6
>>> x > y
False
>>> x >= y
True
>>> x == y
True
>>> x != y
False
>>> x >> y
0
>>> x > 6 and y > 6
False
>>> x == 6 and y == 6
True
>>> x == 6 or y == 6
True
>>> x == 6 or y == 8
True
>>> not x
False
>>> x = True
>>> not x
False
>>> x == y not x == 6
SyntaxError: invalid syntax
>>> msg = "Hello Ram, How are you ?"
>>> 'x' in msg
False
>>> 'x' not in msg
True
>>> 'Ram' in msg
True
>>> 'Ram' not in msg
False
>>> x = 1012125464564
>>> 4 in x
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    4 in x
TypeError: argument of type 'int' is not iterable
>>> x = 7
>>> y = 7
>>> z = x
>>> x
7
>>> y
7
>>> z
7
>>> x == y == z
True
>>> #1, 2, 3
>>> id(7)
2503821388272
>>> id(8)
2503821388304
>>> id(9)
2503821388336
>>> id(10)
2503821388368
>>> id(x)
2503821388272
>>> id(y)
2503821388272
>>> id(z)
2503821388272
>>> x = 12
>>> y = 12
>>> z = 12
>>> a = x
>>> b = y
>>> c = a
>>> d = z
>>> id(12) == id(12) == id(12)
True
>>> 5 == 5
True
>>> x is y
True
>>> x is d
True
>>> x is c
True
>>> msg = 'h'
>>> id('h')
2503823929392
>>> id('h')
2503823929392
>>> id('h')
2503823929392
>>> id('h')
2503823929392
>>> id('he')
2503859295984
>>> id('he')
2503859295984
>>> id('he')
2503859295984
>>> id('hell')
2503859296176
>>> id('hell')
2503859296176
>>> id('hell')
2503859296176
>>> id('hello')
2503859295920
>>> id('hello')
2503859295920
>>> id('hello')
2503859295920
>>> id('hello how are you ?')
2503859213616
>>> id('hello how are you ?')
2503859279392
>>> id('hello how are you ?')
2503859213536
>>> id('hello how are you ?')
2503859279072
>>> id('hello how are you ?')
2503859213456
>>> msg = "hello how are you ?"
>>> text = msg
>>> msg == text
True
>>> msg is text
True
>>> msg_2 = "hello how are you ?"
>>> msg == msg_2
True
>>> msg is msg_2
False
>>> num = 12
>>> num += 5
>>> num
17
>>> num -= 3
>>> num
14
>>> num = num / 4
>>> num
3.5
>>> num **= 4
>>> num
150.0625
>>> id(hello)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    id(hello)
NameError: name 'hello' is not defined
>>> id("hello")
2503859296368
>>> id("hello")
2503859296368
>>> id("hel lo")
2503859295792
>>> id("hel lo")
2503859295728
>>> id("hel lo")
2503859296112
>>> 