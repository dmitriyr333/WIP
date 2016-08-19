''' selection sort'''

def selection_sort( arr ):
    
    # first loop over all the elements
    for i in range( len( arr) ) :
        is_smallest = i

        # second loop; starts only on first loop's index
        for j in range( i, len(arr) ) :
            if arr[j] < arr[is_smallest]:
                is_smallest = j

        # switch values
        arr[is_smallest], arr[i] = arr[i], arr[is_smallest]

    return arr

if __name__ == '__main__' :
    print selection_sort( [5,4,6,0,2] )