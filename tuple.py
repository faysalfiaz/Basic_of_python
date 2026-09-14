# tuple is immutable --> we cannot change it if we create once
marks = (10,50,30,45,90,79)
# we cannot change value by using index
print(marks,type(marks))

# tup = (1,)!! if we donot use , then it is taken as int
# print using index
print(marks[2])

# print count how many time a value have in tuple
print(marks.count(10))

# print index
print(marks.index(50))

print(marks[1:3])