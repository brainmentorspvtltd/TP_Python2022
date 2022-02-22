# w - it will create a new file if file does not exist
# it will overwrite the file if file already exists
# file = open('file_2.txt','w')
# data = "Hello this is file handling..."
# data = "This is python demo..."
# file.write(data)

# file = open('file_2.txt','a')
# data = ["hello\n","how are you ?\n"]
# file.writelines(data)
# file.close()

# x - it will create a new file if file does not exist
# it will raise error if file already exists
file = open('file_3.txt','x')
data = "This is x mode"
file.write(data)
file.close()