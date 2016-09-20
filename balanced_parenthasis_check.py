# find if all parenthesis are in correct sequence

def balance_check( s ):
	length = len(s)

	if length % 2 != 0:
		return False

	stack   = []
	opening = set( [ '(','[','{' ] )
	match   = set( [ ('(',')'), ('[',']'), ('{','}') ] )

	for item in s:
		if item in opening:
			stack.append( item )
		else:
			prior_item = stack.pop()
			if (prior_item, item) not in match:
				return False

	return stack == []



'''test'''
print( balance_check('[](){([[[]]])}(')
