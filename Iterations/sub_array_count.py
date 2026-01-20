def subarray_count(arr,k):
    prefix_sum = 0
    prefix_map = {0:1} #store frequency: earliest index
    count = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]


        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return count

arr = [1, 2, 3]
k = 3
print(subarray_count(arr,k))
