# Finding duplicates can also be implemented using hash maps, check voter_check.py in Hash-Tables folder under Data-Structures folder
def count_frequency(nums):
    #creating an empty dictionary
    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0) + 1
    return freq
def find_duplicate(num_list):
    num_dict = count_frequency(num_list)
    for num,occurance in num_dict.items():
        if occurance > 1:
            return num, occurance
    return -1, -1
#print(find_duplicate([1,2,3,1,5]))
number, occurance = find_duplicate([1,2,3,5,5])
if occurance == -1:
    print("No Duplicates")
else:
    print(f"{number} has duplicate values, occured {occurance} times.")
