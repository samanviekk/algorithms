'''def countOcc(arr, n):
    count = 0
    for i in range(0, len(arr) - 1):
        if arr[i] == n:
            count += 1

    return count

arr = [1, 3, 0, 0, 0 , 3, 3]
print(countOcc(arr, 3))
'''
def countOccStr(s, n):
    count = 0
    for i in s:
        if i == n:
            count += 1
    return count

s = 'sreechae'
print(countOccStr(s, 'e'))