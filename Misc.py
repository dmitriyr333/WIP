
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

'''
	Inheritance
'''
class Character:
	def __init__(self, hair = None):
		self.hair = hair

	def __str__( self ):
		return "Hair is: {0}.".format(self.hair)

class Cook( Character ):
	def __init__( self, hair = None, hat = None):
		Character.__init__(self, hair)
		self.hat = hat
		
	def __str__( self ):
		return Character.__str__(self) + " And {0} hat.".format(self.hat)
		

mike = Cook('brown', 'pointy')
print mike
