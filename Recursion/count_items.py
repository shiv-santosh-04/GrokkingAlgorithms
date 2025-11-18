def count_items(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_items(arr[1:])

print(count_items([1,2,4,3]))