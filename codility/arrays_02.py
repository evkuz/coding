# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# Сдвинуть каждый элемент массива вправо на n шагов

def solution(A, K):
    # write your code in Python 3.6
    N = len(A)
    # b = []
    buf = A[N - 1]

    for j in range(K):
        buf = A[N - 1]
        for i in range(N - 1, -1, -1):
            if i > 0:
                A[i] = A[i - 1]
            # A[i] = A[N - i]
            else:
                A[0] = buf
    return A


A = [3, 8, 9, 7, 6]
K = 3
solution(A, K)
print(*A)