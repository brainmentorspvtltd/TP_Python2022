def even(num):
    return num % 2 == 0

# output = even(6)
# print(output)

numbers = [i for i in range(1,11)]
result = list(filter(even, numbers))
print(result)