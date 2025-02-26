# this topic about the tuple 
# creat tuple 
fruites=("apple","banan","orange","apple")
print(fruites)
# unpaking tuple with variable 
a, b, c, d=fruites
print(a, b, c, d)
# accessing elemant
print(fruites[0])
# slicing elemant
print(fruites[0:3])
# length tuple 
print(len(fruites))
# tuple methods 
# count ()
print(fruites.count("apple"))
# index ()
print(fruites.index("banan"))
# checking item 
print("apple" in fruites)
# looping throught tuple 
for fruites in fruites:
    print(fruites)
# concatenation tuple 
fruites1=("apple","banan","orange","apple")
combine=fruites1+("charry","graps")
print(combine)
# immutable tuple 
fruites1[0]=("date",)
print(fruites1)

