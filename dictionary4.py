# dictionary creation 
dict_table={
    "name":"tajulislam",
    "age":21,

}
print(dict_table)

# # accessing value 
print(dict_table["name"])

# # adding / updating 
dict_table["name"]="khan"
print(dict_table)

# # removing key value pairs 
del dict_table["name"]
print(dict)

# # chcking if a key Exists 
if "tajulislam" in dict_table["name"]:
    print("the name is exsiste !")

# # dictionary length 
print(len(dict_table))

# # clearing a dictionary 
dict_table.clear()
print(dict_table)

# # coping a dictionary 
new_table=dict_table.copy()
print(new_table)

# # looping through dictionary 
# # only for key 
for key in dict_table:
    print(key)

# # only for value 
for values in dict_table.values():
    print(values)

# only for item 
for key,values in dict_table.items():
    print(key,values)

for items in dict_table.items():
    print(items)

# # nested dictionries 
dict_table1={
    "person1":{"anme":"Taj",
               "age":22,
               },
    "person2":{"name":"khan",
               "age":23,
               },
}
print(dict_table1["person1"])
print(dict_table1["person2"]) 

# # dirctionary methods 
# keys ()
print(dict_table.keys())
# items()
print(dict_table.items())
# get()
print(dict_table.get("name"))
# pop()
print(dict_table.pop("age"))
# popitem()
print(dict_table.popitem())
# update()
dict_table.update({"name":"Ahmad"})
print(dict_table)
# setdefault()
dict_table.setdefault("name","taj")
print(dict_table)
# fromkeys()
new_table=dict_table.fromkeys({"name":"taj",
                               "age":22,})
print(new_table)