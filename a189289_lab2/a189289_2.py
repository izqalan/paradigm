myTuple = ('Jane','23','Female')
print(myTuple)

# object destructuring
(Name, Age, Gender) = myTuple

myNewTuple = myTuple[:1] + myTuple[2:]

myList = list(myTuple) 
myList.pop(1)

print(myNewTuple)
print(myList)
