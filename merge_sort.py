def merge_sort( arr ):
    out = []
    if len(arr) < 2 :
        return arr

    mid = len(arr) // 2

    left = merge_sort( arr[0:mid] )
    right = merge_sort( arr[ mid: ] )
    i = 0
    j = 0

    while i < len( left ) and j < len( right ):
        if left[ i ] > right[ j ]:
            out.append( right[j] )
            j += 1
        else:
            out.append( left[ i ] )
            i += 1
    
    out += left[i:]
    out += right[j:]
    
    return out

print( merge_sort( [5,4,3,9,0] ) ) 