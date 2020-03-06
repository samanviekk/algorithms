def remove_duplicates(arr):
    pre = 0
    curr = 1
    while curr < len(arr):
        if arr[curr] == arr[pre]:
            curr = curr + 1
        elif (curr - pre) > 1:
            pre = pre + 1
            arr[pre] = arr[curr]
            curr = curr + 1
        else:
            curr = curr + 1
            pre = pre + 1
    del arr[pre+1:]
    return arr


def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[k - 1] != nums[i]:
            nums[k] = nums[i]
            k = k + 1
    del nums[k:]
    return k

testarr = [0, 0, 0, 0, 1, 3, 4]
remove_duplicates(testarr)
print(testarr)

A = [0, 0, 0, 0, 1, 3, 4]
removeDuplicates(A)
print(A)


