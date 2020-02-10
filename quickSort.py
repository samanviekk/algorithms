def choosePivot(alist, s, e):
    return s

def quickSort(alist, s, e):
    if s >= e:
        return
    pi = choosePivot(alist, s, e)
    p = partition(alist, s, e, pi)
    quickSort(alist, s, p - 1)
    quickSort(alist, p + 1, e)
    return

def partition(alist, s, e, pi):
    pivot = alist[pi]
    left = s + 1
    right = e # b;se we placed the first ele in the last index

    done = False
    while left <= right:
        while left <= right and alist[left] <= pivot:
            left = left + 1
        while alist[right] >= pivot and right >= left:
            right = right - 1

        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]
    alist[s], alist[right] = alist[right], alist[s]
    return right

    '''
    while left < right:
        while alist[left] < pivot:
            left += 1
        while alist[right] > pivot:
            right -= 1
        if left < right:
            alist[left], alist[right] = alist[right], alist[left]
            left += 1
            right -=1

    alist[left], alist[e] = alist[e], alist[left]
    
    return left
'''

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist, 0, len(alist) - 1)
print(alist)