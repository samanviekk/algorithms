def reverse(arr, s, e):
    if s >= e:
        return
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp
    reverse(arr, s + 1, e - 1)


def rotateArray(arr, d):
    reverse(arr, 0, d)
    reverse(arr, d + 1, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)

arr = [1, 2, 3, 4, 5, 6, 7]
rotateArray(arr, 3)
print(arr)

'''
# Number of Test Cases
T = int(input())
# fore each test case, call the rotateArray
for i in range(T):
    # Array Size and RotateBy values
    line = input().split()
    N = int(line[0])
    R = int(line[1])
    # Read Array Values
    listValues = map(int, input().split())
    arr = list(listValues)
    # Now that you have inputs, call the function
    rotateArray(arr, R)
    print(arr)
'''