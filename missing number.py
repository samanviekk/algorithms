def missingNumber(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing = missing ^ i ^ num
    return missing


A = [8,6,4,2,3,5,7,0,1]
print(missingNumber(A))