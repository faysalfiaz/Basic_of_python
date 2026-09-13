# # list : mutable
# # In list we can store multiple type of data
# marks = [30,45,632,'A',32.5]
# # print(marks)
# # # length 
# # print(len(marks))
# # # index
# # print(marks[0])

# # slicing a list --->list[st:end]
# print(marks[0:3])

# # add value last
# marks.append(100)
# print(marks)

# # add in a particular position
# marks.insert(0,90)
# print(marks)

# # check value exit or not
# print(97 in marks)

Faysal = [2, 1, 3]

Faysal.sort()  # sorts in ascending order

Faysal.sort(reverse=True)  # sorts in descending order

Faysal.reverse()  # reverses list

Faysal.insert(3, 30)  # insert element at index

Faysal.remove(1)  # removes first occurrence of element

Faysal.pop(3)  # removes element at idx

# None function : Return nothing