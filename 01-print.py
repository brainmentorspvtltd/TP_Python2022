a = 6
b = 7.0
c = a + b
print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)


print("Sum is %d"%c)
#print("Sum is %f"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {2} is {0}".format(c,a,b))
