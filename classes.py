class A:
	def __init__(self):
		print 'init'
	def __call__(self):
		print 'call'
		
a = A() # prints init ==> initializes object/instance
a()     # prints call ==> calls a function call operator. It is called when instance is called.
