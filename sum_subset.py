def sum_subset(nums, sum):
    res = []
    myset = []
    sum_subset_helper(nums, 0, sum, myset, res)
    return res

def sum_subset_helper(nums, i, sum, myset, res):
    if sum == 0:
        res.append(myset[:])
        return
    if i == len(nums):
        return

    # include
    myset.append(nums[i])
    sum_subset_helper(nums, i + 1, sum - nums[i], myset, res)

    # exclude
    myset.pop()
    sum_subset_helper(nums, i + 1, sum, myset, res)


nums = [1, 2, 3]
res = sum_subset(nums, 3)
print(res)