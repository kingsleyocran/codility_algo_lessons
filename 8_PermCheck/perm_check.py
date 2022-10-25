
# Same as Perm Missing Element except that you are just return 0 or 1 as checks.
def solution(A):
    # Edge case
    if (len(A) == 0):
        return 1

    A.sort()

    for i in range(0, len(A)):
        if A[i] != i + 1:
            return 0
    
    return 1