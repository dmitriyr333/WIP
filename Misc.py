
'''
  read intpu from stdin until there are no more
'''

import sys

for line in sys.stdin():
  # do something


'''
  Enumerate
'''
lst = ['a', 'b', 'c']

for index, value in enumerate(lst):
	print str(index) + value

'''
	Reverse range iteration loop
'''
for numb in xrange(10,0,-1):
	print numb
