def fact(x):
    #base case
    if x <= 1:
        return 1
    #recursion case
    else:
        return x * fact(x-1)

#call fact function
print(fact(3))