'''def findPeek(arr):
    s = 0
    e = len(arr) - 1
    if arr[s] < arr[e]:
        return arr[e]
    while s < e:
        mid = s + (e - s) // 2
        if arr[mid] < arr[mid + 1]:
            s = mid + 1
        else:
            e = mid
    return arr[s]

'''


def findPeakElement(nums) -> int:




testarr= [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(testarr))
