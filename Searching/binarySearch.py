def binary_search(arr,item):
    step = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 #floor division
        guess = arr[mid]
        step+=1
        if guess == item:
            print(f"steps taken:{step}")
            return mid
        elif guess <= item:
            low = mid + 1
        else:
            high = mid - 1
    return -1 #if no element if found,end of list

my_list = [1,5,7,8,9,10,15,25] # sorted list
print(f"Binary_search: 7 found at index",binary_search(my_list,7))