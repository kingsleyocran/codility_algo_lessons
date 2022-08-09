
"""SOLUTION 1"""
def solution(N): 
    #convert N to binary str
    N = bin(N).replace("0b", "")

    #split N, binary str to list
    splt = list(N)

    #define count and maxCount values
    count = 0
    maxCount = 0

    for k in range (1, len(splt)):
        #count your zeros,
        if int (splt[k]) == 0:
            count += 1

        #but if you meet a 1, compare your maxCount and count
        #if 1 doesn't end zeros we return the maxCount, here maxCount is the zeros with and end   
        elif int (splt[k]) == 1:
            maxCount = max(count, maxCount)
            count = 0
            
    return maxCount


"""SOLUTION 2"""          
def solution(N):
    return len(max(format(N, 'b').strip('0').split('1')))