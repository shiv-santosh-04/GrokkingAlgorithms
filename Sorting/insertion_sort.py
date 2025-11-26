def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1

        while j >=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = temp
    return arr
print(insertion_sort([1,3,2,7,5,10,6]))