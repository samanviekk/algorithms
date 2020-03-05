# using two pointers and works only for sorted list
def two_sum(alist, x):
    s = 0
    e = len(alist) - 1
    res = []
    while s < e:
            sum = alist[s] + alist[e]
            if sum == x:
                res.append(alist[s])
                res.append(alist[e])
                return res
                s = s + 1
                e = e - 1
            elif sum < x:
                s = s + 1
            else:
                e = e - 1
    return res


# using hash
def two_sum1(nums, x):
    mymap = {}

    for i in range(len(nums)):
        sum = x - nums[i]
        if sum in mymap:
            #return [mymap[sum], i]
            return [sum, nums[i]]
        mymap[nums[i]] = i
    return None


def has_three_sum(A, t):
    #return any(two_sum1(A, t - a) for a in A)
    for i in range(len(A)):
        result = two_sum1(A[i+1:], t - A[i])
        print(result)
        if result != None:
            result.append(A[i])
            return result
    return None



alist = [1, 2, 4]
print(two_sum(alist, 6))
nums = [3, 2, 4]
print(two_sum1(nums, 6))
A = [2, 3, 5, 7, 11]
print(has_three_sum(A, 16))
