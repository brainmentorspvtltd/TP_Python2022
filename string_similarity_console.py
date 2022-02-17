Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> text = "hello world, this is #python #programming...!!!!"
>>> str.maketrans()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    str.maketrans()
TypeError: maketrans expected at least 1 argument, got 0
>>> str.maketrans('')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str.maketrans('')
TypeError: if you give only one argument to maketrans it must be a dict
>>> str.maketrans('','',text)
{104: None, 101: None, 108: None, 111: None, 32: None, 119: None, 114: None, 100: None, 44: None, 116: None, 105: None, 115: None, 35: None, 112: None, 121: None, 110: None, 103: None, 97: None, 109: None, 46: None, 33: None}
>>> str.maketrans('','',string.punctuation)
{33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None, 40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None, 64: None, 91: None, 92: None, 93: None, 94: None, 95: None, 96: None, 123: None, 124: None, 125: None, 126: None}
>>> table = str.maketrans('','',string.punctuation)
>>> text.translate(table)
'hello world this is python programming'
>>> tokens = text.split()
>>> tokens
['hello', 'world,', 'this', 'is', '#python', '#programming...!!!!']
>>> text = text.translate(table)
>>> tokens = text.split()
>>> tokens
['hello', 'world', 'this', 'is', 'python', 'programming']
>>> stopwords = ["is","this","am","that","the"]
>>> stopwords
['is', 'this', 'am', 'that', 'the']
>>> tokens
['hello', 'world', 'this', 'is', 'python', 'programming']
>>> words = []
>>> for token in tokens:
	if token not in stopwords:
		words.append(token)

		
>>> words
['hello', 'world', 'python', 'programming']
>>> 