def linear_search(arr, item):
    for i in range(len(arr)):
        if item == arr[i]:
            return i
    return -1

result = linear_search([1,2,3,4,5], 3)
if result != -1:
    print("Element Found at index:", result)
else:
    print("Element Not Found")