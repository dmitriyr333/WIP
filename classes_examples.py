class A:
    def __init__(self):
		print( 'init' )
	def __call__(self):
		print( 'call' )
		
a = A() # prints init ==> initializes object/instance
a()     # prints call ==> calls a function call operator. It is called when instance is called.



class Log:
    def __init__(self, level):
        self._level = level

    def __call__(self, message):
        print("{}: {}".format(self._level, message))

log_info = Log("info")
log_warning = Log("warning")
log_error = Log("error")

log_info('Just informational message')