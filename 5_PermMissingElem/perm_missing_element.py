
def solution(A):
    # Edge case
    if (len(A) == 0):
        return 1

    A.sort()

    for i in range(0, len(A)):
        if A[i] != i + 1:
            return (i + 1)
    
    return (len(A) + 1)