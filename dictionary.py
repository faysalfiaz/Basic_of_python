# dictionary {key ===> value}
# there have no index
marks = {"math":99, "physics":97,"chemistry":99}
print(marks,type(marks))
# change value
marks["physics"] = 100
print(marks["physics"])

# print using loops
for key in marks :
    print(key,marks[key])