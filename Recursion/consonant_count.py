def consonant_count(str1):

    # base case:
    if str1 == "": #empty string
        return 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    # recursive case
    if str1[0].isalpha() and str1[0] not in vowel:
        count = 1
    else:
        count = 0
    return count + consonant_count(str1[1:])

print(consonant_count("What are you doing?"))