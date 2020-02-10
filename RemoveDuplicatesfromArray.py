def remove_duplicates(arr):
    pre = 0
    curr = 1
    while curr < len(arr):
        if arr[curr] == arr[pre]:
            curr = curr + 1

        else:
            pre = pre + 2
            arr[pre] = arr[curr]
            curr = curr + 1
            pre = pre + 1
        else:
            curr = curr + 1
            pre = pre + 1

    return len(arr)


testarr = [0, 0, 0, 0, 1, 3, 4]
res = remove_duplicates(testarr)
print(res)
print(testarr)


