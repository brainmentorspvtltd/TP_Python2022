# Global Variables
x = 12
y = 10

def add():
    # Local Variable
    global x,y
    x = 5
    y = 8
    z = x + y
    print("Sum is",z)

def sub():
    # Local Variable
    z = x - y
    print("Sub is",z)

add()
sub()