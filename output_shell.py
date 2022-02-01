Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: D:\Trainings\TPDDL_Python\01-print.py ================
13.0
Sum is 13.0
Sum of 6 and 7.0 is 13.0
Sum is 13
Sum of 6 and 7 is 13
Sum is 13.0
Sum of 6 and 7.0 is 13.0
Sum of 6 and 7.0 is 13.0
Sum of 6 and 7.0 is 13.0
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/02-print.py ==================
Sum is...
>>> 
=================== RESTART: D:\Trainings\TPDDL_Python\01-print.py ==================
Traceback (most recent call last):
  File "D:\Trainings\TPDDL_Python\01-print.py", line 4, in <module>
    print(c)
NameError: name 'c' is not defined
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/02-print.py ==================
Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.8333333333333334
Mul of 5 and 6 is 30
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/02-print.py ==================
Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.83
Mul of 5 and 6 is 30
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/02-print.py ==================
Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.83
Mul of 5 and 6 is 30

Sum of {a} and {b} is {c}
Sub of {a} and {b} is {d}
Div of {a} and {b} is {e}
Mul of {a} and {b} is {f}

>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/02-print.py ==================
Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.83
Mul of 5 and 6 is 30

Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.8333333333333334
Mul of 5 and 6 is 30

>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/02-print.py ==================
Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.83
Mul of 5 and 6 is 30

Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.83
Mul of 5 and 6 is 30

>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/02-print.py ==================

Sum of 5 and 6 is 11
Sub of 5 and 6 is -1
Div of 5 and 6 is 0.83
Mul of 5 and 6 is 30

>>> msg = "Hello Ravi"
>>> msg
'Hello Ravi'
>>> print(msg)
Hello Ravi
>>> msg = "Hello "Ravi""
SyntaxError: invalid syntax
>>> msg = "Hello ", "Ravi"
>>> print(msg)
('Hello ', 'Ravi')
>>> msg = 'Hello "Ravi"'
>>> print(msg)
Hello "Ravi"
>>> msg = "Hello 'Ravi'"
>>> print(msg)
Hello 'Ravi'
>>> msg = "Hello 'Ravi'"
>>> print(msg)
Hello 'Ravi'
>>> msg = '''"Hello 'Ravi'"'''
>>> print(msg)
"Hello 'Ravi'"
>>> msg = "Hello \"\Ravi\"\"
SyntaxError: EOL while scanning string literal
>>> msg = "Hello \"Ravi\""
>>> print(msg)
Hello "Ravi"
>>> path = "C:\new\abc\text"
>>> print(path)
C:
ewbc	ext
>>> path = "C:\\new\\abc\\text"
>>> print(path)
C:\new\abc\text
>>> path = "C:/new/abc/text"
>>> print(path)
C:/new/abc/text
>>> path = r"C:\new\abc\text\c\d\f\h\f\s\f\h\h\s"
>>> print(path)
C:\new\abc\text\c\d\f\h\f\s\f\h\h\s
>>> #raw string
>>> path = f"D:\Trainings\TPDDL_Python"
>>> path
'D:\\Trainings\\TPDDL_Python'
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================
Sum is 154
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================
Sum is 154
>>> c
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================
Sum is 154
Traceback (most recent call last):
  File "D:/Trainings/TPDDL_Python/03-print.py", line 5, in <module>
    print(c + 20)
NameError: name 'c' is not defined
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================
Traceback (most recent call last):
  File "D:/Trainings/TPDDL_Python/03-print.py", line 3, in <module>
    print("Sum is",c = a + b)
TypeError: 'c' is an invalid keyword argument for print()
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================
Sum is 154
174
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================
Traceback (most recent call last):
  File "D:/Trainings/TPDDL_Python/03-print.py", line 7, in <module>
    print(f"Sum of {a} and {b} is {c := a + b}")
NameError: name 'c' is not defined
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================
Sum of 120 and 34 is 154
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================

Sum is 154
Sub is 86
Div is 3.5294117647058822
Mul is 4080

>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================

Sum is 154
Sub is 86
Div is 3.5294117647058822
Mul is 4080

>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/03-print.py ==================

Sum is 154
Sub is 86
Div is 3.5294117647058822
Mul is 4080

154 86 3.5294117647058822 4080
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/04-input.py ==================
Enter your name : Ravi
Hello Ravi
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/04-input.py ==================
Enter your name : Ravi
Hello Ravi
Enter first number : 34
Enter second number : 32
Sum is 3432
>>> fnum
'34'
>>> fnum + snum
'3432'
>>> type(fnum)
<class 'str'>
>>> type(snum)
<class 'str'>
>>> 
=================== RESTART: D:/Trainings/TPDDL_Python/04-input.py ==================
Enter your name : Ravi
Hello Ravi
Enter first number : 32
Enter second number : 23
Sum is 55
>>> 
================ RESTART: D:/Trainings/TPDDL_Python/05-data_types.py ================
12 12001020120121020102121 34343
>>> 
================ RESTART: D:/Trainings/TPDDL_Python/05-data_types.py ================
12 12001020120121020102121 34343
4.509908 4.509908596749857
>>> 
================ RESTART: D:/Trainings/TPDDL_Python/05-data_types.py ================
12 12001020120121020102121 34343
4.509908 4.509908596749857
(2+6j)
>>> 
================ RESTART: D:/Trainings/TPDDL_Python/05-data_types.py ================
12 12001020120121020102121 34343
4.509908 4.509908596749857
(2+6j)
hello how are you ?
Traceback (most recent call last):
  File "D:/Trainings/TPDDL_Python/05-data_types.py", line 27, in <module>
    msg = bytes(msg)
TypeError: string argument without an encoding
>>> 
================ RESTART: D:/Trainings/TPDDL_Python/05-data_types.py ================
12 12001020120121020102121 34343
4.509908 4.509908596749857
(2+6j)
hello how are you ?
b'hello how are you ?'
>>> 
================ RESTART: D:/Trainings/TPDDL_Python/05-data_types.py ================
12 12001020120121020102121 34343
4.509908 4.509908596749857
(2+6j)
hello how are you ? आप कैसे हैं?
b'hello how are you ? \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82?'
>>> msg.decode()
'hello how are you ? आप कैसे हैं?'
>>> import sys
>>> sys.getsizeof(msg)
83
>>> msg
b'hello how are you ? \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82?'
>>> sys.getsizeof(0)
24
>>> sys.getsizeof(1)
28
>>> sys.getsizeof(2)
28
>>> sys.getsizeof(2121212112)
32
>>> sys.getsizeof(212121211)
28
>>> sys.getsizeof(2121212110)
32
>>> sys.getsizeof(99999999)
28
>>> sys.getsizeof(999999999)
28
>>> sys.getsizeof(9999999999)
32
>>> sys.getsizeof(99999999999999999)
32
>>> sys.getsizeof(9999999999999999999)
36
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
1
2
3
4
5
6
7
8
9
10
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
1
2
3
4
5
6
7
8
9
10
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
1
2
3
4
5
6
7
8
9
10
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
Traceback (most recent call last):
  File "D:/Trainings/TPDDL_Python/loop_1.py", line 7, in <module>
    print(i)
NameError: name 'i' is not defined
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
1
2
3
4
5
6
7
8
9
10
2
4
6
8
10
12
14
16
18
20
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
1
2
3
4
5
6
7
8
9
10
2
4
6
8
10
12
14
16
18
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
--------------------
1
2
3
4
5
6
7
8
9
10
--------------------
2
4
6
8
10
12
14
16
18
20
--------------------
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_1.py ===================
0
Inside Loop
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
Outside Loop
--------------------
1
2
3
4
5
6
7
8
9
10
--------------------
2
4
6
8
10
12
14
16
18
20
--------------------
10
9
8
7
6
5
4
3
2
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/loop_2.py ===================
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4
>>> 