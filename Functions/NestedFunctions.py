def calc():
    x = 12
    y = 13
    def add():
        z = x + y
        print(z)

    def sub():
        z = x - y
        print(z)

    return add, sub

functions = calc()
functions[0]()
functions[1]()