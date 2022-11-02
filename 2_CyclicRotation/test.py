"""

"""

testCases = [
    
    {
        'input': {
            'A': [1, 2, 3, 4],
            'K': 4
        },
        'output': [1, 2, 3, 4]
    },
    {
        'input': {
            'A': [0, 0, 0],
            'K': 4
        },
        'output': [0, 0, 0]
    },
    {
        'input': {
            'A': [-4],
            'K': 4
        },
        'output': [-4]
    },
    {
        'input': {
            'A': [3, 4, 2, 5, 7, 4],
            'K': 2
        },
        'output': [7, 4, 3, 4, 2, 5 ]
    },
    {
        'input': {
            'A': [3, 8, 9, 7, 6],
            'K': 3
        },
        'output': [9, 7, 6, 3, 8]
    },
]


def evaluateTest(tests):
    countPass = 0
    countFail = 0

    for i in range(0, len(tests)):

        print('TEST: ', i + 1)

        result = solution(**tests[i]['input'])

        if (result == tests[i]['output']):
            countPass += 1
            print("PASSED")
        else:
            countFail += 1
            print("FAILED")

        print('')

    print(f"TEST: {len(tests)} \tPASS: {countPass} \tFAIL: {countFail}")


def solution(A, K):
    if(len(A) == 0 or len(A) == K):
        return A

    if(len(A) == 1 or K == 0):
        return A
    
    K = K % len(A)
    result = A[-K:] + A[ 0 : (len(A) - K) ]
    return result

evaluateTest(testCases)
