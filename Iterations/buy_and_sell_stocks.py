def buy_and_sell(prices):
    res = 0
    n = len(prices)
    print(n)
    for i in range(0, n-1):
        for j in range(i+1, n):

            res = max(res, prices[j] - prices[i])
    return res
print(buy_and_sell([1,5,2,7,8]))
