def count_zero(x,count=0):
    if x==0:
        return count
    elif x % 10 == 0:
        return count_zero(x//10,count+1)
    else:
        return count_zero(x // 10, count)

print(count_zero(10900))

