counter = int(input("How many tables you want to print ?"))

for j in range(counter):
    num = int(input("Enter a number : "))

    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

    print("==================")
