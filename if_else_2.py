a,b,c = 10,12,34

if a > b and b > c:
    print("A is greatest")
elif b > a and b > c:
    print("B is greatest")
else:
    print("C is greatest")


#Expression
result = "A" if a > b and b > c else "B" if b > a and b > c else "C"
print(result, "is greatest")
