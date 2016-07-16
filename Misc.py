
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




''' 
Is there any reason for a class declaration to inherit from object?

I just found some code that does this and I can't find a good reason why.

class MyClass(object):
    # class code follows...
    
Yes, this is a 'new style' object. It was a feature introduced in python2.2.
New style objects have a different object model to classic objects, and some things won't work properly 
with old style objects, for instance, super(), @property and descriptors. 
See this article for a good description of what a new style class is:
	http://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
'''


''' defaultdict '''

 from collections import defaultdict
 d = defaultdict(<type>)
