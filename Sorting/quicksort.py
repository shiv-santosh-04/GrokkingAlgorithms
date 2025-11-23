def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left_arr = [i for i in arr[1:] if i <= pivot]
        right_arr = [i for i in arr[1:] if i > pivot]

    return quicksort(left_arr) + [pivot] + quicksort(right_arr)
print(quicksort([5,2,1,3]))