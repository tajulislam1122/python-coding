# this is set data structur 
# creat set 
fruite={"apple","orang","mango"}
print(fruite)

# creat empty set 
set_empty={}
print(set_empty)

# length of set 
print(len(fruite))

# clear a set 
print(fruite.clear())

# methods of the set 
# add a data 
fruite.add("banana")
print(fruite)

# remove and elemant 
fruite.remove('orang')
print(fruite)

# union of two set 
set1={1,2,3,4}
set2={4,5,6,7}
union=set1|set2
print(union)

# intersection set
set1={1,2,3,4}
set2={4,5,6,7}
intersection=set1&set2
print(intersection)

# check if a elamant 
if "apple" in fruite:
    print("yes this elemant exsist !")

# looping through a set 
for fruit in fruite:
    print(fruit)