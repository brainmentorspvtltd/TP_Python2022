temps = [34.56,28.7,37.6,33.4,30.6,29.6]
f = list(map(lambda cel : 9/5 * cel + 32, temps))
print(f)

numbers = [i for i in range(1,11)]
e = list(filter(lambda x : x % 2 == 0, numbers))
print(e)