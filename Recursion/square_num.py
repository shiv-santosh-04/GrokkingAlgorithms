def num_square(num):
    #odd sum method
    if num == 0:
        return 0
    else:
        return (2*num - 1) + num_square(num-1)

print(num_square(5))
