f = open("demo.txt", "r")
# data = f.read(5)
LINE1 = f.readline()
print(LINE1)
# print(data)
# print(type(data))
f.close()

# 'r': open for reading (default)
# 'w': open for writing, truncating the file first
# 'x': create a new file and open it for writing
# 'a': open for writing, appending to the end of the file if it exists
# 'b': binary mode
# 't': text mode (default)
# '+': open a disk file for updating (reading and writing)