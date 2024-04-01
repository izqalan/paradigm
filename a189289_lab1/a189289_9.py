textfile = open('testfile.txt', 'w')
textfile.write("I am a test file.\n")
textfile.write("This is a new line of text.\n")
textfile.close()

f = open('testfile.txt', 'r')
string = f.read(1)

print(string)

# print(f.read())

print(f.readline())

f.close()
