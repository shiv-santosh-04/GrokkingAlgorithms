def twoSum(arr, target):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            sum = arr[i] + arr[j]
            if sum == target:
                print("There exists a pair whose sum equals target:",target)
                return arr[i], arr[j]
    print("No pair exists whose sum is eual to the target")
    return 0,0

arr = [0,-1,2,-3,1]
tar = -2
val1, val2 = twoSum(arr,tar)
if val1 == 0:
    print("No pair exists whose sum is equal to target",tar)
else:
    print(f"{val1} and {val2} have sum equal to {tar}")
