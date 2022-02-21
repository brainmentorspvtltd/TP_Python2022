Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def greet():
	yield "hi"
	yield "hello"
	yield "bye"

	
>>> greet()
<generator object greet at 0x000001239E488EB0>
>>> next(greet())
'hi'
>>> next(greet())
'hi'
>>> next(greet())
'hi'
>>> msg = greet()
>>> next(msg)
'hi'
>>> next(msg)
'hello'
>>> next(msg)
'bye'
>>> next(msg)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    next(msg)
StopIteration
>>> def outer():
	def inner_1():
		return "Hello"
	def inner_2():
		return "Bye"
	return inner_1(), inner_2()

>>> outer()
('Hello', 'Bye')
>>> def outer():
	def inner_1():
		return "Hello"
	def inner_2():
		return "Bye"
	return inner_1, inner_2

>>> outer()
(<function outer.<locals>.inner_1 at 0x000001239E50AE50>, <function outer.<locals>.inner_2 at 0x000001239E50ADC0>)
>>> def outer():
	x = 12
	y = 22
	def inner_1():
		return "Hello"
	def inner_2():
		return "Bye"
	return x,y

>>> outer()
(12, 22)
>>> def outer():
	x = 12
	y = 22
	def inner_1():
		return "Hello"
	def inner_2():
		return "Bye"
	return inner_1, inner_2

>>> outer()
(<function outer.<locals>.inner_1 at 0x000001239E50AF70>, <function outer.<locals>.inner_2 at 0x000001239E50ADC0>)
>>> outer()[0]()
'Hello'
>>> outer()[1]()
'Bye'
>>> 