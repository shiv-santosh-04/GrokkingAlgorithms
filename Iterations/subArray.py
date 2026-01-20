def longest_subarray_sum(arr,k):
    prefix_sum = 0
    prefix_map = {0:-1}
    max_len = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if (prefix_sum - k) in prefix_map:
            length = i - prefix_map[prefix_sum - k]
            max_len = max(max_len, length)


        if (prefix_sum - k) not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len

arr = [10, 5, 2, 7, 1, 9]
k = 10
print(longest_subarray_sum(arr, k))

