def shellSort(array):
    "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
    gap = len(array) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(array)):
            j = i
            while j >= gap and array[j - gap] > array[j]:
                array[j], array[j - gap] = array[j - gap], array[j]
                j -= gap
        gap //= 2
    return array

print shellSort([5,4,3,8,0])