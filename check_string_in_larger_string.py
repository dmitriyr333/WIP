'''
  Given small string 'source' and large string 'target', design an algorithm 
  to find all permutations of the shorter string within the longer one.
  Print location of each permutation.
'''

source = 'abbc'
target = 'cbabadcbbabbcbabaabccbabc'

length_source = len(source)
length_target = len(target)

for index in range( 0,length_target-3 ):
	new_target = target[index:index+length_source] # just get what we need 
	# print new_target
	if (sorted(source) == sorted(new_target)):
		print new_target
