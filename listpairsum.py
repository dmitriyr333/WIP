def foo( arr, k):
    seen = set()
    output = set()
    length = len(arr)





    for element in range(length):
        target_minus = max(k,arr[element]) - min(k,arr[element])

        #print( target
        if target_minus not in seen:
            seen.add( arr[element] )
        else:
            output.add( (min(target_minus, arr[element]),max(target_minus, arr[element])))

        target_plus  = max(k,arr[element]) + min(k,arr[element])

        if target_plus not in seen:
            seen.add( arr[element] )
        else:
            output.add( (min(target_plus, arr[element]),max(target_plus, arr[element])))

    return output

if __name__ == '__main__':
    arr = [1,7,5,9,2,12,3]
    arr2 = [9,1,2,8,3,7,4,6,5,5,13,14,11,13,-1]
    k   = 2

    # print( foo( arr, k )

    print( foo( arr2, 10)
