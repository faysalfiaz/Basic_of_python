# dictionary {key ===> value}
# there have no index
# we can change value (mutable)
# donot allow duplicate keys

info ={
    "key":"value",
    "name":"faysal_Ahmed",
    "learning":"python",
    "age":35,
    "is_adult":True,
    "maks":94.4,
    "subject":["python","c","java"],
    "topics":("dict","set"),
}
# print(info["name"])


# change value
info["name"] = "Faysal Ahmed Ramim"
# null dictionary
null_dict = {}
null_dict["name"] ="FaysalFaiz"
# print(null_dict)


# nested dict 
student = {
    "name":"Ramim Rizwan",
    "subject":{
        "phy":51,
        "chem":30,
        "math":25
    }
}
print(student["subject"]["chem"])

# Dictionary Methods (here myDict is dictionary name)

# myDict.keys() #returns all keys
# myDict.values() #returns all values
# myDict.items() #returns all (key, val) pairs as tuples
# myDict.get( "key"" ) #returns the key according to value
# myDict.update( newDict ) #inserts the specified items to the dictionary

# new_dict = {"city":"delhi"}
# student.upadte(new_dict)
# we cannot store set in here 