''' recursively reverse the string '''

def reverse( s ):
	if len(s) == 1:
		return s
	else:
		return reverse( s[1:] ) + s[0]
		
		
print reverse('hello world')