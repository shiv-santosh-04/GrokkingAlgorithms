def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    max_rest = find_max(arr[1:])
    return arr[0] if arr[0] > max_rest else max_rest
print(find_max([1,5,7]))