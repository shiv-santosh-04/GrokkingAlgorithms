# check whether the given list is anagram or not

def anagram(words):

    #word is a list/array here
    # first word
    word = words[0]
    
    if len(word) == 0:
        return 0
    
    # sort the characters of the first word
    sorted_word = sorted(word)
    # print(f"Sorted first word: {sorted_word}")
    # check if all other words have the same characters
    for i in range(1, len(words)):
        if sorted(words[i]) != sorted_word:
            return 0
    
    return 1

l1 = ['cat','act']
result = anagram(l1)

if result:
    print(f"{l1} is anagram")
else:
    print(f"{l1} is not anagram")
        



