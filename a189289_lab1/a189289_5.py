"""
print 
*|*|*|*|*
*********
*|*|*|*|*
*********
*|*|*|*|*
"""

# def pattern_1():
#   print("*|*|*|*|*")

# def pattern_2():
#   print("*********")


def pattern(subpattern):
  subpattern_length = len(subpattern)
  # floor division
  pattern = subpattern * (9 // subpattern_length)
  # add trailing characters to pattern
  # if length of subpattern is enough to fill 9 characters then no need to add trailing characters
  # if length of subpattern is not enough to fill 9 characters then add trailing characters
  # this will break if subpattern length is >= 5
  r = 9 % subpattern_length
  pattern += subpattern[:r]
  return pattern


def main():
  for i in range(5):
    if i % 2 == 0:
      print(pattern("*|"))
    else:
      print(pattern("*"))
  
main()