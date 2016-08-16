
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


''' read in csv file '''
import csv

with open( __filename__, 'rb') as csvfile:
    data_reader = csv.reader( csvfile ):
        for row in data_reader:
            # do something
        else:
            # end of file

''' generator vs iterators '''
this_generator = (x*2 for x in range(3)) # generator => can only be used once. Once used, they forget their value. It is not stored in memory!!!
this_iterator  = [x*2 for x in range(3)] # can be used many times

print this_iterator
print this_generator

print 'running generator first time'
for i in this_generator :
    print i

print 'second time, this will not run'
for i in this_generator :
    print i

print 'running iterator multiple times'
for i in this_iterator :
    print i
for i in this_iterator :
    print i


''' Yield is a keyword that is used like return, except the function will return a generator.

    To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is a bit tricky :-)

    Then, your code will be run each time the for uses the generator.

    Now the hard part:

    The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

    The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy an "if/else" anymore.
'''
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
# generator object createGenerator at 0xb7555c34>
for i in mygenerator:
     print(i)
#0
#2
#4


