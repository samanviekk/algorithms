def containsNearbyAlmostDuplicate(nums, k, t):
    res = []
    for i in range(len(nums)):
        res.append((nums[i], i))
    res.sort()
    print(res)
    i = 0; j = 1
    while j < len(res):
        if abs(res[i][0] - res[j][0]) <= t and abs(res[i][1] - res[j][1]) <= k:
            return True
        else:
            if abs(res[i][0] - res[j][0]) <= t:
                j = j + 1
            else:
                j = j + 1
                i = i + 1
    return False

nums = [1, 3, 6, 2]

k = 1
t = 2
print(containsNearbyAlmostDuplicate(nums, k, t))