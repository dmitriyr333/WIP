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
        print( str( self.value ),
        if self.right:
            self.right.in_order_node()


    def post_order_node( self ):
        if self.left:
            self.left.in_order_node()
        if self.right:
            self.right.in_order_node()
        print( str( self.value ),


    def levels_node( self ):
        level = [ self ]

        while level:
            current_level = []
            for branch in level:
                print( branch.value,
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


    def post_order( self ):
        if not self.root:
            return False
        else:
            self.root.post_order_node()


    def levels( self ):
        if not self.root:
            return False
        else:
            self.root.levels_node()


# checks if binary search tree is valid/correct
def is_valid_BST( branch, mini_root_value = None, maxi_root_value = None ):
    if not branch:
        return True

    # FALSE: left child value is greater then branch
    if mini_root_value and mini_root_value >= branch.value:
        return False

    # FALSE: right child value is less then branch
    elif maxi_root_value and maxi_root_value <= branch.value:
        return False

    # recursion
    else:
        return( is_valid_BST( branch.left, mini_root_value, branch.value )
               and is_valid_BST( branch.right, branch.value, maxi_root_value ) )


# trim BST between given min and max values
def trim_bst( root, min_val, max_val ):
    # if empty
    if not root:
        return

    # post-order traverse
    root.left  = trim_bst( root.left,  min_val, max_val )
    root.right = trim_bst( root.right, min_val, max_val )

    # all is good
    if min_val <= root.value <= max_val:
        return root

    # if right node is greater than max_val
    if root.value > max_val:
        return root.left

    # if left node is less then min_val
    if root.value < min_val:
        return root.right




''' test '''
if __name__ == '__main__':
    # print( 'here'
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

    # creating incorrect BST
    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(3)

    a2.left = a3
    a2.right = a1


    # b.print_root()

    # b.in_order()
    # print
    # b.post_order()
    # print
    # b.levels()
    # print
    # print( is_valid_BST(b.root)
    # print
    # print( is_valid_BST(a2)

    trim_bst( b.root, 10, 31)
    b.in_order()

