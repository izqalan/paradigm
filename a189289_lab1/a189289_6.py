"""
print
*|*|*|*|* H *|*|*|*|* H *|*|*|*|*
********* H ********* H *********
*|*|*|*|* H *|*|*|*|* H *|*|*|*|*
********* H ********* H *********
*|*|*|*|* H *|*|*|*|* H *|*|*|*|*
==========+===========+==========
*|*|*|*|* H *|*|*|*|* H *|*|*|*|*
********* H ********* H *********
*|*|*|*|* H *|*|*|*|* H *|*|*|*|*
********* H ********* H *********
*|*|*|*|* H *|*|*|*|* H *|*|*|*|*
"""

# pattern generator
# input: *| or *
def pattern_gen(subpattern):
  subpattern_length = len(subpattern)
  if subpattern_length > 9:
    print("Womp womp: subpattern length is too long")
    return
  
  subpattern_length = len(subpattern)

  pattern = subpattern * (9 // subpattern_length)
  # remove trailing characters
  r = 9 % subpattern_length
  pattern += subpattern[:r]
  return pattern

def row(pattern, separator, copies):
  # at the eend of each copy print char 'H' before continuing
  # at the last copy no need to print char 'H'
  # if copies == 3 then print 'H' 2 times
  # *|*|*|*|* H *|*|*|*|* H *|*|*|*|*
  pattern_str = ''
  for i in range(copies):
    pattern_str += pattern
    if i != copies - 1:
      pattern_str += separator

  return pattern_str

def main():
  # copy horizontally 3 times
  copies = 3

  # copy vertically 2 times
  vcopies = 2
  
  for i in range(5*vcopies):
    if i % 2 == 0:
      print(row(pattern_gen("*|"), " H ", copies))
    elif i == 5:
      print(row(pattern_gen("="), " + ", copies))
    else:
      print(row(pattern_gen("*"), " H ", copies))

main()