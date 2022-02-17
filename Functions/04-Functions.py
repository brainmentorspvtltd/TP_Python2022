# *args - dynamic arguments / variable length argument
def add(*x):
    # print(x)
    # print(sum(x))
    s = 0
    for n in x:
        s += n
    print(s)

add(4,5)
add(4,5,5,7)
add(2,34,5,7,8,34,4,6)
add()
add(4)

# **kwargs - keyword variable length arguments
def person(**details):
    print(details)

person(id=101, name="Ram", salary=45000)
person(id=102, name="Shyam", dept="IT")
person(id=120, name="Naman", salary=40000, dept="HR")
