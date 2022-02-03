n = int(input("Enter the max range : "))
sum = 0
for i in range(n+1):
    if i % 2 == 0:
        sum += i

print("Sum is :",sum)
