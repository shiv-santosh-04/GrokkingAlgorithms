def check_palindrome(x):
    if len(x) <=1:
        return True
    elif x[0] == x[-1]:
        return check_palindrome(x[1:-1])
    else:
        return False

#main function
result = check_palindrome('level')
if result == True:
    print("is plaindrome")
else:
    print("is not plaindrome")
