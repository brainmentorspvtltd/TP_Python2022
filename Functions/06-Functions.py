def calc(num_1, num_2, opr):
    expression = num_1 + opr + num_2
    result = eval(expression)
    print(result)

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = int(input("Enter your choice: "))

num_1 = input("Enter first number : ")
num_2 = input("Enter second number : ")

operators = {
    1 : "+",
    2 : "-",
    3 : "/",
    4 : "*"
}

opr = operators.get(ch)
calc(num_1, num_2, opr)