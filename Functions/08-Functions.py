def calc(num_1, num_2, opr):
    expression = num_1 + opr + num_2
    result = eval(expression)
    return result

def takeInput():
    ch = int(input("Enter your choice: "))
    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")
    # packing
    return ch, num_1, num_2

def main():
    operators = {
        1: "+",
        2: "-",
        3: "/",
        4: "*"
    }
    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    # unpacking
    ch, num_1, num_2 = takeInput()
    opr = operators.get(ch)
    result = calc(num_1, num_2, opr)
    print("Result is",result)

main()