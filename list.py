# list
# In list we can store multiple type of data
marks = [30,45,632,'A',32.5]
# print(marks)
# # length 
# print(len(marks))
# # index
# print(marks[0])
# slicing a list --->list[st:end]
print(marks[0:3])

# add value 
marks.append(100)
print(marks)

# add in a particular position
marks.insert(0,90)
print(marks)
# check value exit or not
print(97 in marks)