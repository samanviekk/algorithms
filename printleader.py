def printLeader(arr):
    current = arr[-1]
    result = []
    result.append(current)
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > current:
            current = arr[i]
            result.append(current)
    for j in range(len(result) - 1, -1, -1):
        print(result[j], end = ' ')

arr = [18, 17, 4, 3 , 5, 2]
printLeader(arr)


