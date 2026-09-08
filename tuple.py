#tuple is immutable --> we cannot change it if we create once
marks = (10,50,30,45,90,79)

print(marks,type(marks))

# print using index
print(marks[2])

# print count how many time a value have in tuple
print(marks.count(10))

# print index
print(marks.index(50))