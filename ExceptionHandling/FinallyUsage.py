import io

try:
    file = open('file_1.txt','w')
    file.write("Hello")
    data = file.read()
    print(data)
except io.UnsupportedOperation:
    print("Operation not supported...")
except FileNotFoundError:
    print("File not found...")
finally:
    print("I will always execute...")
    file.close()
    print("File Closed...")