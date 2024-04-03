# TK2053 Programming Paradigm Lab 2
# Author: Izqalan Nor'Izad
# Matric: a189289

personal_tuple = [('name', 'izqalan'),('age', 25), ('drinks', 'negroni')]
personal_dict = dict(personal_tuple)

def get_key(value):
  for k,v in personal_dict.items():
    if v == value:
      return k
  return 'key not found'

print(get_key('izqalan'))
print(get_key(25))
print(get_key('negroni'))