Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: D:/Trainings/TPDDL_Python/chat_1.py =================
Enter your message : hello
Hello User
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/chat_1.py ===================
Enter your message : hello
Hello User
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/chat_1.py ===================
Enter your message : HeLLo
I don't understand
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/chat_1.py ===================
Enter your message : HELLO
Hello User
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/chat_1.py ===================
Enter your message : hello
Hello User
Enter your message : Hello
Hello User
Enter your message : HELlo
Hello User
Enter your message : bye
Bye User
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/chat_2.py ===================
Enter your message : hi
Hello User
Enter your message : hey
Hello User
Enter your message : hello
Hello User
Enter your message : hi there
Hello User
Enter your message : bye
Bye User
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/chat_2.py ===================
Enter your message : hi
Hey There
Enter your message : hey
Hi There
Enter your message : hello
Hey
Enter your message : hi there
Hi
Enter your message : hello
Hi There
Enter your message : bye
Bye User
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2022, 2, 4, 16, 35, 26, 627488)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2022, 2, 4, 16, 35, 36, 378525)
>>> from datetime import datetime as dt
>>> dt.now()
datetime.datetime(2022, 2, 4, 16, 36, 38, 656400)
>>> dt.now().date()
datetime.date(2022, 2, 4)
>>> dt.now().time()
datetime.time(16, 36, 59, 243534)
>>> date = dt.now().date()
>>> time = dt.now().time()
>>> print(date)
2022-02-04
>>> print(time)
16:37:16.861352
>>> date.strftime("%d/%m/%y")
'04/02/22'
>>> date.strftime("%d/%m/%Y")
'04/02/2022'
>>> date.strftime("%d %B, %Y")
'04 February, 2022'
>>> date.strftime("%d %b, %Y")
'04 Feb, 2022'
>>> date.strftime("%d %b, %Y, %a")
'04 Feb, 2022, Fri'
>>> date.strftime("%d %b, %Y, %A")
'04 Feb, 2022, Friday'
>>> time.strftime("%H:%M:%S, %p")
'16:37:16, PM'
>>> 
==================== RESTART: D:/Trainings/TPDDL_Python/chat_2.py ===================
Enter your message : hey
Hey There
Enter your message : hi
Hello There
Enter your message : hello
Hello
Enter your message : date
Date is 04 Feb, 2022, Fri
Enter your message : time
Time is 16:42:00, PM
Enter your message : tell me date
Date is 04 Feb, 2022, Fri
Enter your message : tell me time
Time is 16:42:05, PM
Enter your message : bye
Bye User
>>> time.strftime("%I:%M:%S, %p")
'04:42:05, PM'
>>> import webbrowser
>>> webbrowser.open("google.com")
True
>>> webbrowser.open("facebook.com")
True
>>> webbrowser.open("twitter.com")
True
>>> msg = "open facebook"
>>> msg.startswith("open")
True
>>> msg.split()
['open', 'facebook']
>>> msg.split()[1]
'facebook'
>>> website_name = msg.split()[1]
>>> msg = "open twitter"
>>> website_name = msg.split()[1]
>>> website_name
'twitter'
>>> webbrowser.open(website_name".com")
SyntaxError: invalid syntax
>>> webbrowser.open(website_name+".com")
True
>>> 