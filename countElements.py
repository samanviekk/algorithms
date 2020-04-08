def countElements(arr):
    lookup = {}
    for i in arr:
        lookup[i] = lookup.get(i, 0) + 1

    res = []
    count = 0
    for i in arr:
        if i in lookup and i+1 in lookup:
            res.append(i)
            count += 1

    print(count)

arr = [1, 1, 2, 2]
countElements(arr)