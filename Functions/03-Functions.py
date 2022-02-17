def add(x=0, y=0):
    z = x + y
    print(f"Sum of {x=} and {y=} is {z=}")

def sub(x=0, y=0):
    z = x - y
    print(f"Sub of {x=} and {y=} is {z=}")

add(4,5)
sub(8,4)

# Keyword Argument
add(x=5, y=7)
add(y=12, x=10)

add()
add(5)
add(x=6)
add(y=7)
