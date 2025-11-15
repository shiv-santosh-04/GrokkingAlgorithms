def sum_of_digits(x):
    if x <= 9:
        return x
    else:
        return (x%10) + sum_of_digits(x//10)
print(sum_of_digits(123))