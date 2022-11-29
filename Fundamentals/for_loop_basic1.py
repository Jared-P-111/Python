
"""print values to 150"""

for i in range(151):
  print(i)

"""print multiples of 5 up to 1000"""

for i in range(1001):
  if i % 5 == 0:
    print(i)

""" Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo """

for i in range(101):
  if i % 5 == 0:
    print("Coding")
  else:
      print(i)

  if i % 10 == 0:
    print("Coding Dojo")
  else:
    print(i)

""" Add odd integers from 0 to 500,000, and print the final sum. """

sum = 0

for i in range(500001):
  if i % 2 != 0:
    sum = sum + i

  if i == 500000:
    print(sum)


""" Print positive numbers starting at 2018, counting down by fours. """

for i in range(2018, 0, -4):
  print(i)

"""
Set three variables: lowNum, highNum, multi. Starting at lowNum
and going through highNum, print only the integers that are a multiple of mult.
For example, if lowNum=2, highNum=9, and multi=3, the loop should print 3, 6, 9 (on successive lines)
"""
00
highNum = 9
multi = 3

for i in range(highNum):
  if i % multi == 0:
    print( "num", i)