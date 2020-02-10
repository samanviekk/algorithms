def squareRoot(k):
    res = 0
    for i in range(1, k + 1):
        if i * i == k :
            return i
        elif i * i < k:
            res = i

    return res

def squareRootBS(k):
    s = 0
    e = k + 1
    res = 0
    while s <= e:
        mid = s + (e - s) // 2
        if mid * mid == k:
            return mid
        elif mid * mid > k:
            e = mid - 1
        else:
            res = mid
            s = mid + 1
    return res


print(squareRoot(16))
print(squareRootBS(16))