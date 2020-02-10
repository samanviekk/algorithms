def dutch_flag_partition(pivot_index, A):
    pivot = pivot_index
    small = 0 ; equal = 0 ; large = len(A)
    while equal < large:
        if A[equal] < pivot:
            A[small], A[equal] = A[equal], A[small]
            small += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            large -= 1
            A[equal], A[large] = A[large], A[equal]

    return -1


A = [1, 2, 3, 1, 2, 3]
dutch_flag_partition(2, A)
print(A)
