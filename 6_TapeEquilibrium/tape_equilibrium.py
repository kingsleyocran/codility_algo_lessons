def solution(A):
    #find head element and sum of the rest, the tail.
    head = A[0]
    tail = sum(A[1:])

    # the difference will be the starting point of the min difference
    minDiff = abs (head - tail)

    #loop through array to find the new min difference
    for i in range(1, len(A) - 1):
        head += A[i]
        tail -= A[i]

        if (abs(head - tail) < minDiff):
            minDiff = abs(head - tail)

    return (minDiff)