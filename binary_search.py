def sorted_binary_search( arr, element ):

    first = 0            # first index
    last  = len(arr) -1  # last index


    while first <= last:
        mid = (first + last) / 2

        # found it !!!
        if arr[ mid ] == element:
            return True

        # go left
        elif arr[ mid ] > element:
            last = mid - 1 # adjust index

        # go right
        else:
            first = mid + 1 # adjust index

    return False



def sorted_binary_search_recursive( arr, element ):

    # base case
    if len(arr) == 0:
        return False


    mid = len(arr) / 2

    if arr[ mid ] == element:
        return True
    elif arr[ mid ] > element:
        return sorted_binary_search_recursive( arr[:mid], element )
    else:
        return sorted_binary_search_recursive( arr[mid + 1:], element )



''' test '''
# print( sorted_binary_search([1,2,3,4,5],8)
print( sorted_binary_search_recursive([1,2,3,4,5],9)


