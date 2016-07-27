class Node( object ):
    def __init__( self, value = None, nextnode = None ):
        self.value = value
        self.nextnode = nextnode

class LinkedList( object ):
    def __init__( self ):
        pass

    ''' display '''
    def display( self, head ):
        start = head

        while start != None:
            print start.value
            start = start.nextnode

        return head

    ''' insert '''
    def insert( self, head, data):
        temp_node = Node( data )

        if head == None:
            head = temp_node # first node
        elif head.nextnode == None:
            head.nextnode = temp_node # second node
        else:
            # multi node linked list
            current = head
            while current.nextnode != None:
                current = current.nextnode
            current.nextnode = temp_node

        return head

    def delete( self, head, data ):
        current = head

        # if we deleting first node
        if current.value == data:
            current = current.nextnode
            return current

        # for everything else...
        while current != None:
            # if we found data in nextnode, then do the magic
            if current.nextnode.value == data:
                current.nextnode = current.nextnode.nextnode
                return head
            # else we have continue with our search
            current = current.nextnode

        # if we reached up to here, no node to delete was found
        return False

    def reverse( self, head ):
        previous = None
        current  = head
        next     = None

        while current != None:
            next = current.nextnode # safe store next node
            current.nextnode = previous
            previous = current
            current = next

        return previous

''' test '''
head = None

myLink = LinkedList()

head = myLink.insert( head, 1 )
head = myLink.insert( head, 2 )
head = myLink.insert( head, 3 )
head = myLink.insert( head, 8 )

head = myLink.display( head )

head = myLink.delete( head, 8)

head = myLink.reverse( head )

head = myLink.display( head )
