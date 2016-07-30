
'''
  read intpu from stdin until there are no more
'''

import sys

for line in sys.stdin():
  # do something

# or...
n, m = map(int,raw_input().split())



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


""" NOTES:
      - requires Python 2.4 or greater
      - elements of the lists must be hashable
      - order of the original lists is not preserved
"""
def unique(a):
    """ return the list with duplicate elements removed """
    return list(set(a))

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

    """ return intesection of ALL elements in the list """
    return set.intersection( *full_list )



def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))

if __name__ == "__main__":
    a = [0,1,2,0,1,2,3,4,5,6,7,8,9]
    b = [5,6,7,8,9,10,11,12,13,14]
    print unique(a)
    print intersect(a, b)
    print union(a, b)


''' List comprehension '''
ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
ListOfThreeMultiples
# [0, 3, 6, 9]


''' Neat way to check if string contains special characters '''
str = 'qA2'
print any(c.isalnum()  for c in str) # True
print any(c.isalpha() for c in str) # True
print any(c.isdigit() for c in str) # True
print any(c.islower() for c in str) # True
print any(c.isupper() for c in str) # True
