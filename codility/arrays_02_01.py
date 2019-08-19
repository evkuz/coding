# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# Сдвинуть каждый элемент массива вправо на n шагов

def solution(A, K):
    # write your code in Python 3.6
    N = len(A)
    # b = []
    buf = A[N - 1]

    for j in range(K):
        buf = A[N - 1]
        for i in range(1, N):
            A[N-i] = A[N - i - 1]
        A[0] = buf
    return A


A = [3, 8, 9, 7, 6]
K = 3
if len(A) > 0:
    solution(A, K)
    print(*A)
else:
    print("Error, empty array")

# The following issues have been detected: runtime errors.

# For example, for the input ([], 0) the solution terminated unexpectedly.
