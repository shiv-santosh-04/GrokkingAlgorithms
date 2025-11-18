def count_vowel(str1):
    # base case
    if str1 == "":
        return 0
    vowel = ['a','e','i','o','u']
    count = 1 if str1[0].lower() in vowel else 0
    return count + count_vowel(str1[1:])

print(count_vowel("Are you"))