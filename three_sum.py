'''Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.'''
def two_sum(nums, x):
    mymap = {}

    for i in range(len(nums)):
        sum = x - nums[i]
        if sum in mymap:
            #return [mymap[sum], i]
            return [sum, nums[i]]
        mymap[nums[i]] = i
    return None


def has_three_sum(A, t):
    for i in range(len(A)):
        result = two_sum(A[i+1:], t - A[i])
        print(result)
        if result != None:
            result.append(A[i])
            return result
    return None


A = [2, -2, 5, 7, 11]
print(has_three_sum(A, 0))
