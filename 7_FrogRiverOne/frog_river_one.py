def solution(X, A):
    
    #create counting array with -1 since we return -1 when the frog can't jump
    B = [-1] * X

    #(A[i] <= X) -> We dont want to go beyond the river
    #Where we have no leaf. So for where we have a leaf A[i] - 1 will be >= 0

    for i in range (0, len(A)):
        if (A[i] <= X and B[A[i] - 1] == -1):
            B[A[i] - 1] = i
    
    m = 0

    for i in range (0, len(B)):
        #if there are no leaf then the frog can't jump
        if(B[i] == -1):
            return (-1)
        
        #find the max in the array B which is our count array
        m = max(m, B[i])

    return m