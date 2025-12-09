def count_frequency(nums):
    #creating an empty dictionary
    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0) + 1
    return freq
numbers_list = [1,1,2,1,3,5,5,3]
#print(count_frequency(numbers_list))
result = count_frequency(numbers_list)
for key, values in result.items():
    print(f"{key} has frequency {values}")
