def maxsum_subarray(A):
    maxsum = A[0]
    cursum = 0

    for i in range(1, len(A)):
        cursum = cursum + A[i]
        if cursum < 0:
            cursum = 0
        elif maxsum < cursum:
            maxsum = cursum

    return maxsum

A = [-2, -3, -4, -1, -2, -1, -5, -3]
print(maxsum_subarray(A))
