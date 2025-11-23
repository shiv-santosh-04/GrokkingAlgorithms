import random
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr)-1)]
        left_arr = [i for i in arr if i < pivot]
        mid_arr = [i for i in arr if i == pivot]
        right_arr = [i for i in arr if i > pivot]

    return quicksort(left_arr) + mid_arr + quicksort(right_arr)
print(quicksort([5,2,1,3]))