a,b = 120,34

#walrus operator :=
#print("Sum is",c := a + b)
#print(c + 20)

#print(f"Sum of {a} and {b} is {(c := a + b)}")

print(f"""
Sum is {(c := a + b)}
Sub is {(d := a - b)}
Div is {(e := a / b)}
Mul is {(f := a * b)}
""")


