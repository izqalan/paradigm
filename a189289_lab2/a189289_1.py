# s = [5,6,7]
# # this will print [5, 6, 7] 7
# # print(s, s[2])

# # this will print 6
# # print(s[-2])

# # update index 1
# s[1] = "foo"

# # this will print [5, 'foo', 7]
# print(s)

# # add "bar" to the end of the list
# s.append("bar")

# # pop "bar"
# xs = s.pop()

# # print "bar"
# print(xs)

# # create list of [0, 1, 2, 3, 4]
# s = list(range(5))
# print(s) 
# # print all elements
# print(s[:])
# # print index 1 to 3-1
# print(s[1:3]) 
# # print index 0 to 3-1
# print(s[:3])
# # print index 3 to end
# print(s[3:]) 

s = 5* [10] 
s[0] += 5 
print(id(s[0]), id(s[1]), id(s[2]), id(s[3]))

print(s)

# print(id(s[0]), id(s[1]), id(s[2]), id(s[3]))

# create list of 3 empty strings
s = [''] * 3
s[2] += 'a' 
print(s)
# print(id(s[0]), id(s[1]), id(s[2]), id(s[3]))


# create 4 empty nested arrays
# [[], [], [], []]
# nested list is mutable
s = [[]] * 4
# add 1 to the first nested array because the value is in []
s[1] += [1]
# this value is mutable even though it is in []
# index 0 will have different memory address than the rest 
s[0] = [4, 1]
print(id(s[0]), id(s[1]), id(s[2]), id(s[3]))
print(s)

