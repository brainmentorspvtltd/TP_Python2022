try:
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))

    add = x + y
    print("Sum is", add)

    sub = x - y
    print("Sub is", sub)

    div = x / y
    print("Div is", div)

    mul = x * y
    print("Mul is", mul)

except ZeroDivisionError as err:
    # print(err)
    print("Cannot divide by zero...")

except ValueError as err:
    # print(err)
    print("Invalid Input...Please enter a number")

except BaseException as ex:
    print("Some error...",ex)