''' web site: http://www.tutorialspoint.com/python/python_reg_expressions.htm '''

''' match '''
#!/usr/bin/python
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print( "matchObj.group() : "), matchObj.group()
   print( "matchObj.group(1) : "), matchObj.group(1)
   print( "matchObj.group(2) : "), matchObj.group(2)
else:
   print( "No match!!" )

'''
  matchObj.group() :  Cats are smarter than dogs
  matchObj.group(1) :  Cats
  matchObj.group(2) :  smarter
'''



''' search '''
#!/usr/bin/python
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print( "searchObj.group() : "), searchObj.group()
   print( "searchObj.group(1) : "), searchObj.group(1)
   print( "searchObj.group(2) : "), searchObj.group(2)
else:
   print( "Nothing found!!")

'''
  matchObj.group() :  Cats are smarter than dogs
  matchObj.group(1) :  Cats
  matchObj.group(2) :  smarter
'''



''' searching vs matching '''
#!/usr/bin/python
import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print( "match --> matchObj.group() : "), matchObj.group()
else:
   print( "No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print( "search --> searchObj.group() : "), searchObj.group()
else:
   print( "Nothing found!!")

'''
  No match!!
  search --> matchObj.group() :  dogs
'''



''' search and replace '''
#!/usr/bin/python
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print( "Phone Num : {}".format( num))

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print( "Phone Num : {}".format( num))

'''
  Phone Num :  2004-959-559
  Phone Num :  2004959559
'''




''' searching for strings using .findinter() '''
string = "I its raining cats and dogs. \nAnd cats. \nMaybe dogs too"
pattern_re = re.compile(r'\w+') # creating an compile object
# for each char in string
for char in string:
    # print( 'char: {}'.format(char) )
    # for each pattern object
    for match in pattern_re.finditer( char ):
      print( 'match: {}, match.group(): {}'.format( match, match.group() ) )
      letter = match.group()
      column = match.start()+1