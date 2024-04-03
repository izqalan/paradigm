mySet1 = {"Postcard","Radio","Telegram"}
# this string will be converted/sliced to a set 
mySet2 = set("A Python Tutorial")
print(mySet1)
print(mySet2)

mySet3 = set(["Perl", "Python", "Java"]) 
print(mySet3)

mySet4 = set(("Apple","Orange","Pear","Pineapple","Apple", "Lemon")) 
print(mySet4)

# This will raise an error
# Because set() can only contain immutable elements
# in this case the set is trying to contain a list
# which list is mutable
mySet5 = set((["Apple","Orange","Pear","Pineapple"],["Perl","Python"]))  
print(mySet5)
