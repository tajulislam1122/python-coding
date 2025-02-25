# List topic
# Create a list []
list=["i'm a list topic !"]
print(type(list))
# accessing Elements
fruits=["apple","orange","banana"]
print(fruits[2])
# list slicing
print(fruits[0:3])
#length of list[]
print(len(fruits))
# checking if an item exists 
print("apple" in fruits)

# List Methods []
# Adding Elements
# append()
fruits.append("charry")
print(fruits)
# extend()
fruits.extend(["groups","ahrote"])
print(fruits)
# insert()
fruits.insert(0,"peach")
print(fruits)

# removing elements 
fruits.remove("apple")
print(fruits)
# pop()
fruits.pop(0)
print(fruits)
# sort()
fruits.sort()
print(fruits)
# sort(reverse=true)
fruits.sort(reverse=True)
print(fruits)
# copy list
list_new=fruits.copy()
print(list_new)
# joining list[]
new_list=fruits+["apple1","orange2"]
print(new_list)
# looping list[]
for fruit in fruits:
    print(fruit)
# list comprehension 
add=[x**2 for x in range(5)]
print(add)