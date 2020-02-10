T = int(input())
#fore each test case, call the rotateArray
for i in range(T):
    #Array Size and RotateBy values
    line = input().split()
    N=int(line[0])
    R=int(line[1])
    #Read Array Values
    listValues = map(int, input().split())
    arr = list(listValues)
    #Now that you have inputs, call the function
    if R > 0 and len(arr) > 0:
        rotateArray(arr, R)
    for j in range(0, len(arr)):
        print(arr[j], end = ' ')
    print()