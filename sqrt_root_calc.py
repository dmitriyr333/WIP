''' calculate sqrt root without build in function '''
def calc_root( num ):
    if num < 1:
        raise ValueError('Enter value greater than 1')
    
    if num == 1:
        return num

    for i in range( 1, (num/2)+2 ):
        if i * i > num:
            return i - 1
# test
for j in range( 15, 18 ):
    print calc_root( j )