from array import array


def solution(A: array, K: int) -> array:
    # Edge cases
    # if len(A) == 0
    if (len(A)/K == 0):
        return A

    # if a rotation = the len of arr
    if (len(A) == 0):
        return A
    
    # if all elements are the same
    if len(set(A)) == 1:
        return A

    # if K = 0  
    if (K == 0):
        return A


    K = K % len(A)
    return A[-K:] + A[:-K]


print(solution([3, 8, 9, 7, 6], 3))
# return [9, 7, 6, 3, 8]