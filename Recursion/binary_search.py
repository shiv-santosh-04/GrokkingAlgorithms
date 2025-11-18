def binary(arr, item, left, right):
    #end of list
    if left > right:
        return -1
    mid = (left + right)//2
    guess = arr[mid]
    # if guess is correct, base case
    if guess == item:
        return mid
    # recursive case 1
    elif guess > item:
        return binary(arr,item,left,mid-1)
    # recursive case 2
    else:
        return binary(arr,item, mid+1, right)

arr = [1,5,7,9,12,15,17]
result = binary(arr,17,0,len(arr)-1)
if result == -1:
    print("Element Not Found")
else:
    print("Element found at index:",result)
