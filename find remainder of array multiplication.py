def findReminder(arr, n):
    m = 1
    for i in range(0, len(arr)):
        m *= arr[i] % n
       # print(m)
    # r = m % n
    return m % n   # return r... this results of overflow
                   # b/se if we multiply n nums and the result is oveflowed

arr = [100, 10, 5, 25, 35, 14]
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print(findReminder(arr, 11))
