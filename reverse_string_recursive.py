''' recursively reverse the string '''

def reverse( s ):
	if len(s) == 1:
		return s
	else:
		# return reverse( s[1:] ) + s[0]
		# OR
		return s[-1] + reverse( s[0:len(s)-1] )
		
		
print( reverse('hello world')
