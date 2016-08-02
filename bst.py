class BinaryTree( object ):
    def __init__ (self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def insert( self, m_data ):

        # no root exist. This is a first element (root)
        if not self:
            return BinaryTree( m_data )

        # we have at least a root already in the tree
        else:

            # go right
            if m_data > self.data:

                # if right already has leaf(s)
                if self.right:
                    return self.right.insert( m_data )

                # else we are inserting the node
                else:
                    self.right = BinaryTree( m_data )
                    return True

            # go left
            else:

                # if left already exist
                if self.left:
                    return self.left.insert( m_data )

                # else we are inserting the node
                else:
                    self.left = BinaryTree( m_data )
                    return True


    def in_order( self ):
        if self:
            if self.left:
                self.left.in_order()

            print str(self.data)

            if self.right:
                self.right.in_order()

    def levels( self ):
        current_level = [self]
        num_of_levels = 0

        while current_level:
            next_level = list() # storing left + right resulst
            num_of_levels += 1

            # iterating over what was found
            for c in current_level:
                print c.data, #in python 2.7 the comma is to show that the string will be printed on the same line

                if c.left:  next_level.append( c.left )
                if c.right: next_level.append( c.right )

            print
            current_level = next_level

        print 'Number of levels: {0}'.format(num_of_levels)


    def find( self, m_data ):

        # if tree is empty
        if not self:
            return False

        # go right
        if m_data > self.data:

            # if right child exist
            if self.right:

                # if we found our data
                if self.right.data == m_data:
                    return True

                # else recursively look for data
                else:
                    return self.right.find( m_data )

            # we aint found shit
            else:
                return False

        # else go left
        else:

            # if left child exist
            if self.left:

                # if we found our data
                if self.left.data == m_data:
                    return True

                # else recursively look for data
                else:
                    return self.left.find( m_data )

            # we aint found shit
            else:
                return False

''' test '''
b = BinaryTree()
b.insert(5)
b.insert(34)
b.insert(23)
b.insert(1)
b.insert(3)
b.insert(4)

# b.in_order()

# print (b.find(7))
# print (b.find(3))

b.levels()



