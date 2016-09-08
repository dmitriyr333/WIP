
'''
  read intpu from stdin until there are no more
'''

import sys

for line in sys.stdin():
  # do something

# or...
n, m = map(int,raw_input().split())



'''
  Enumerate ---> don't forget second argument'
'''
lst = ['a', 'b', 'c']

for index, value in enumerate(lst,0):
	print str(index) + value

'''
	Reverse range iteration loop
'''
for numb in xrange(10,0,-1):
	print numb




'''
	Inheritance
'''
class Character( object ):
	def __init__(self, hair = None):
		self.hair = hair

	def __str__( self ):
		return "Hair is: {0}.".format(self.hair)

class Cook( Character ):
	def __init__( self, hair = None, hat = None):
		super( self.__class__, self).__init__( hair)
		self.hat = hat

	def __str__( self ):
		return Character() + " And {0} hat.".format(self.hat)


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


''' removes duplicates i.e. [4,4] '''
print list( set( [1,2,3,4,4,5] ) )


""" return the intersection (of elements present) of two lists """
print list( set( [1,2,3,4,4,5] ) & set( [5,6] ) )

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
    for i in range(3):
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
# generator object createGenerator at 0xb7555c34>
for i in mygenerator:
     print(i)
#0
#2
#4


''' Accessing an attribute using a variable '''
l = ['a','b','c']
# using variable 'append'
append_variable = 'append'
getattr(l,append_variable)('d')
# it is the same as >>> #l.append('d')
# >>> ['a','b','c','d']


''' strings, print in the middle
str.center(width[, fillchar])
    Parameters
width -- This is the total width of the string.
fillchar -- This is the filler character.
'''
print 'WELCOME'.center(40, '-')
# >>> ------WELCOM-------


''' lambda / filter / map'''
test_lambda = (lambda x,y: x*y)
print test_lambda(3,4)
# >>> 12
lst = [1,2,3]
print map(lambda x: x**2, lst)
# >>> [1, 4, 9]
print filter (lambda x: x%2 == 0, lst)
# >>> [2]






''' decorators '''
# Function decorators enable the addition of new functionality 
# to a function without altering the function’s original functionality.
# or another explanation
# “wrappers” that let you execute code before and 
# after the function they decorate without modifying the function itself.

# example
import datetime

# decorator expects another function as argument
def logger(func_to_decorate):

    # A wrapper function is defined on the fly
    def func_wrapper():

        # add any pre original function execution functionality 
        print("Calling function: {} at {}".format(func_to_decorate.__name__, datetime.datetime.now()))

        # execute original function
        func_to_decorate()

        # add any post original function execution functionality
        print("Finished calling : {}".format(func_to_decorate.__name__))

    # return the wrapper function defined on the fly. Body of the 
    # wrapper function has not been executed yet but a closure 
    # over the func_to_decorate has been created.
    return func_wrapper

def print_full_name():
    print("My name is John Doe")

>>>decorated_func = logger(print_full_name)
>>>decorated_func
# the returned value, decorated_func, is a reference to a func_wrapper
<function func_wrapper at 0x101ed2578>
>>>decorated_func()
# decorated_func call output
Calling function: print_full_name at 2015-01-24 13:48:05.261413
# the original functionality is preserved
My name is John Doe
Finished calling : print_full_name




''' closures '''
# Closures can be used for maintaining states
def make_log(level):
    def _(message):
        print("{}: {}".format(level, message))
    return _

log_info = make_log("info")
log_warning = make_log("warning")
log_error = make_log("error")




''' lists '''
# finding index of array
>>> li
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
>>> li.index("example")
5
# inserting element
>>> li.insert(2,True)
>>> li
['a', 'b', True, 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

# delete element
>>> del li[1]
>>> li
['a', True, 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
>>> li.remove('new')
>>> li
['a', True, 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

# sort
>>> arr.sort()  # <--- permanently sort arr
>>> sorted(arr) # <--- original arr remains the same, only displays temp sorted arr

# copy lists ( use [:] )
>>> li_new = li[:]
# this will NOT work: li_new = li <--- because it will only set a name to existing list









''' printing floats '''
print( '{0:0.1f}'.format(mean) ) # will print 8.3

''' finding mode of an array of numbers '''
sorted( arr )
counted_arr = [ arr.count(x) for x in arr ] # array of counted numbers
arr[ counted_arr.index( max( counted_arr ) ) ]


# weak typing and strong typing
# unit tests 
# stack and heap memory