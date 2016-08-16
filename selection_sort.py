''' Yield is a keyword that is used like return, except the function will return a generator.'''
'''
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
