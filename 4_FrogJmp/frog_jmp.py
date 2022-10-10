def solution(X, Y, D):
    count = 0

    distance = Y - X

    rem = distance % D
    count = distance // D

    if (rem == 0):
        return (count)
    else:
        return (count + 1)

print(solution(10, 10, 30))