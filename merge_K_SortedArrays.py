import heapq

def mergeSortedArrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    print(sorted_arrays_iters)

    for i, it in enumerate(sorted_arrays_iters):
        first_ele = next(it, None)
        if first_ele is not None:
            heapq.heappush(min_heap, (first_ele, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_ele = next(smallest_array_iter, None)
        if next_ele is not None:
            heapq.heappush(min_heap, (next_ele, smallest_array_i))
    return result

# Another approach using builtins
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(myheapq.merge(*sorted_arrays))


A = [[2, 8, 9, 12],
     [1, 3, 5, 7],
     [4, 6, 7, 8]
     ]
print(mergeSortedArrays(A))
