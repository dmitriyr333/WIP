class Solution:
    # Write your code here
    def __init__( self, lst=None ):
        # if nothing was passed to us
        if lst == None:
            self.queue = []
            self.stack = []
        # else just initialize passed argument to instance's attribute
        else:
            self.queue = list( lst ) # FIFO
            self.stack = list( lst ) # LIFO
        
    def pushCharacter( self, elem ):
        return self.stack.append( elem )
    
    def enqueueCharacter( self, elem ):
        return self.queue.append( elem )
    
    def popCharacter( self ):
        try:
            return self.stack.pop() # pop last element
        except IndexError:
            raise IndexError('No more items left in the stack')
            
    def dequeueCharacter( self ):
        try:
            return self.queue.pop( 0 ) # pop first element
        except IndexError:
            raise IndexError("No more items left in the queue")
            
            
if __name__ == '__main__':
  # read the string s
  s=raw_input()
  #Create the Solution class object
  obj=Solution()   
  
  l=len(s)
  # push/enqueue all the characters of string s to stack
  for i in range(l):
      obj.pushCharacter(s[i])
      obj.enqueueCharacter(s[i])
      
  isPalindrome=True
  '''
  pop the top character from stack
  dequeue the first character from queue
  compare both the characters
  ''' 
  for i in range(l / 2):
      if obj.popCharacter()!=obj.dequeueCharacter():
          isPalindrome=False
          break
  #finally print whether string s is palindrome or not.
  if isPalindrome:
      sys.stdout.write ("The word, "+s+", is a palindrome.")
  else:
      sys.stdout.write ("The word, "+s+", is not a palindrome.")
