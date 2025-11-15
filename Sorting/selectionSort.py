def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] <= smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#selection sort function
def selectionSort(arr):
    newArr = []
    #copy the original array into copiedArr
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = find_smallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))#pop removes the element from index
    return newArr

arr = [2,8,1,5,7]
print("Before Sorting array is:",arr)
sorted_arr = selectionSort(arr)
print('After Sorting array is:',sorted_arr)