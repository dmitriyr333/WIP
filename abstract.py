
'''
	Abstract Classes
'''
from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
    
#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price
        #print( title
        
    def display( self ):
        print( "{0}{1}{2}".format(self.title, self.author, self.price)


new_novel=MyBook('title','author',12)
new_novel.display()
