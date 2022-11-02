
#testCases
#Algo

testCases = [
    {
        'input': {
            'A': [3, 8, 9, 7, 6],
            'K': 3
        },
        'output': [9, 7, 6, 3, 8]
    },
    {
        'input': {
            'A': [1, 2, 3, 4],
            'K': 4
        },
        'output': [1, 2, 3, 4]
    },
    {
        'input': {
            'A': [1, 2, 3, 4, 5, 6, 7],
            'K': 6
        },
        'output': [2, 3, 4, 5, 6, 7, 1]
    },
    {
        'input': {
            'A': [1, 2, 3],
            'K': 0
        },
        'output': [1, 2, 3]
    },
    {
        'input': {
            'A': [-1, 0 , 2, 4],
            'K': 2
        },
        'output': [2, 4, -1, 0 ]
    }
]

def evaluateTests (tests):
    countPassed = 0
    countFailed = 0

    for i in range(0, len(tests)):
        result = solution(**tests[i]['input'])

        print ('TEST: ', i)
        print (f"Input: {tests[i]['input']['A']},  {tests[i]['input']['K']}")
        print ('Expected Output: ', tests[i]['output'])
        print ('Actual Output: ', result)
        

        if(tests[i]['output'] == result):
            countPassed += 1
            print('TEST PASSED')
        else:
            countFailed += 1
            print('TEST FAILED')
        
        print('')

    print(f"TOTAL TESTS: {len(tests)}\t\tPASSED: {countPassed}\t\tFAILED: {countFailed}")
    print('ALL TESTS PASSED') if countPassed == len(tests) else print('SOME TESTS FAILED')
    



# def solution(A, K):
#     if K == 0 or K == len(A):
#         return A

#     arr = A[(K - 1):] + A[0: (len(A)) - K]
#     return arr

def solution(A, K):
    # Edge cases
    # if len(A) == 0
    if (len(A) == 0):
        return A
    
    # if all elements are the same
    if (len(A) > 0):
        if len(set(A)) == 1:
            return A

    # if K = 0  
    if (K == 0):
        return A

    K = K % len(A)
    return A[-K:] + A[:-K]
    
evaluateTests(testCases)