def merge(A, B):
    i = len(A) - 1
    A.extend(B)
    j = len(B) - 1
    k = len(A) - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i = i - 1
            k = k - 1
        else:
            A[k] = B[j]
            j = j - 1
            k = k - 1

    while j >= 0:
        A[k] = B[j]
        j = j - 1
        k = k - 1
    while i >= 0:
        A[k] = A[i]
        i = i - 1
        k = k - 1


A = [-4, 3]
B = [-2, -2]
merge(A, B)
print(A)
print('length = ', len(A))