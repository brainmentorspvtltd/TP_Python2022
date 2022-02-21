def temp_convert(c):
    return 9/5 * c + 32

def km_to_m(km):
    return km * 1000

# temp = 34.5
# print(temp_convert(temp))

temps = [34.56,28.7,37.6,33.4,30.6,29.6]
# f = []
# for t in temps:
#     f.append(temp_convert(t))
# print(f)

kms = [4,45,6,8,8,4,3,5,7]

f = list(map(temp_convert, temps))
print(f)

ms = list(map(km_to_m, kms))
print(ms)
