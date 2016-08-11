class Node( object ):
    def __init__( self, cargo = None, left = None, right = None ):
        self.value = cargo
        self.left  = left
        self.right = right

    def insert_node( self, value ):
        # check if value already exist; exit with False if it does;
        # no dups allowed
        if self.value == value:
            return False
        else:
            # go right
            if value > self.value:
                # if node has right child
                if self.right:
                    return self.right.insert_node( value )
                # no right child. Create one
                else:
                    self.right = Node( value )
                    return True
            # go left
            else:
                if self.left:
                    return self.left.insert_node( value )
                else:
                    self.left = Node( value )
                    return True

    def in_order_node( self ):
        if self.left:
            self.left.in_order_node()
        print str( self.value ),
        if self.right:
            self.right.in_order_node()

    def levels_node( self ):
        level = [ self ]

        while level:
            current_level = []
            for branch in level:
                print branch.value,
                if branch.left:  current_level.append( branch.left  )
                if branch.right: current_level.append( branch.right )
            level = current_level
            print





''' BST class '''
class BST( object ):
    def __init__( self, root = None ):
        self.root = root

    def insert( self, value ):

        # first node in our tree
        if not self.root:
            self.root = Node( value )
            return True
        # root already exist
        else:
            return self.root.insert_node( value )


    def in_order( self ):
        if not self.root:
            return False
        else:
            self.root.in_order_node()

    def levels( self ):
        if not self.root:
            return False
        else:
            self.root.levels_node()



def is_valid_BST( root, mini = None, maxi = None ):
    if not root:
        return True
    if mini and mini >= root.value:
        return False
    elif maxi and maxi <= root.value:
        return False
    else:
        return( is_valid_BST(root.left, mini, root.value)
               and is_valid_BST(root.right, root.value, maxi))




''' test '''
if __name__ == '__main__':
    # print 'here'
    b = BST()
    b.insert(11)
    b.insert(6)
    b.insert(8)
    b.insert(19)
    b.insert(4)
    b.insert(10)
    b.insert(5)
    b.insert(17)
    b.insert(43)
    b.insert(49)
    b.insert(31)

    # 11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 3

    # b.print_root()

    # b.in_order()
    # b.levels()
    print is_valid_BST(b.root)
