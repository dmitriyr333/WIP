class MyClass( object ):
	def __init__( self, arr = None ):
		if arr == None:
			self.arr = []
		else:
			self.arr = list(arr)
			
	def buubleSort( self ):
		
		length = len(self.arr)
		sorted_array = False
		
		while not sorted_array:
			sorted_array = True # assume that array is sorted
			for i in range(0,length-1):
				# found unsorted pair
				if self.arr[i] > self.arr[i+1]:
					sorted_array = False # this will resume WHILE loop
					self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
	
	def __str__( self ):
		return str( self.arr )
		
''' lets test it out '''
b = MyClass([1,2,3,5,4])
b.buubleSort()
print b
