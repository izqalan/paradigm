# TK2053 Programming Paradigm Lab 1
# Author: Izqalan Nor'Izad
# Matric: a189289

def create_file(filename):
    try:
      file = open(filename, 'w')
      file.close()

    except:
      print('Womp womp: Unable to create file')

def write_file(filename, content):
  try:
    file = open(filename, 'w')
    file.write(content)
    file.close()
  except:
    print('Womp womp: Unable to write to file')

def read_file(filename):
  try:
    file = open(filename, 'r')
    string = file.read()
    file.close()
    return string
  except:
    print('Womp womp: Unable to read file')

def main():
  create_file("python_file.txt")
  write_file("python_file.txt", "Izqalan Nor'Izad\nNetwork Technology")

  file = read_file("python_file.txt")
  for i in range(3):
    print(file)

# run main func
main()