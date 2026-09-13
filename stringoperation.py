# string
str1 = "This is string"
str2 = 'hello'
str3 = """This is another"""

# newline  /n
# tab /t
# concatinate -->str1+str2
# using index we cannot change the value

# replace 
name = "Faysal"
print(name.replace("Faysal","Thor"))
own_name = "Ramim"
print(own_name.replace("Ra","Fa"))

# check for presence
print('R' in own_name) # here "in" is a reserved words

str = "I am studing python from youtube."

str.endswith("youtube.")  # returns true if string ends with substr

str = str.capitalize()  # capitalizes 1st char (assign back to str to update it)

str.replace("studing", "Learning")  # replaces all occurrences of old with new

str.find("python")  # returns 1st index of 1st occurrence

str.count("am")  # counts the occurrence of substr in string