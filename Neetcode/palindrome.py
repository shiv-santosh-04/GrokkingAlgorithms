def palindrome(s):

    #s is the string to check.
    left = 0
    right = len(s) - 1

    while left<right:

        while left<right and not s[left].isalnum():
            left+=1

        while left<right and not s[right].isalnum():
            right-=1

        if s[left].lower() != s[right].lower():
            return False

        left+=1
        right-=1
    return True

str1 = "A man, a plan, a canal, Panama"
result = palindrome(str1)

if result:
    print(f"{str1} is a palindrome")
else:
        print(f"{str1} is not a palindrome")