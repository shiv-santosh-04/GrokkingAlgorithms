def countSubsets(arr, index=0):
    # Base Case:- reached end of list
    if index == len(arr):
        return 1

    include = countSubsets(arr,index+1)

    exclude = countSubsets(arr,index+1)

    return include + exclude
print(countSubsets([1,2]))

