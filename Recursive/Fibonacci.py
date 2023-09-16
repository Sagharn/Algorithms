# O(n)
def fib_linear(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib_linear(n - 1, b, a + b)


n = int(input())
nth_fib = fib_linear(n)
print(nth_fib)

print("--------------------------")


# O(log n)

def multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result


def power(matrix, n):
    size = len(matrix)
    if n == 1:
        return matrix

    half_power = power(matrix, n // 2)
    result = multiply(half_power, half_power)

    if n % 2 == 1:
        result = multiply(result, matrix)

    return result


def fib_log_n(n):
    if n == 0:
        return 0

    base_matrix = [[1, 1], [1, 0]]
    result_matrix = power(base_matrix, n - 1)

    return result_matrix[0][0]


n = int(input())
nth_fib = fib_log_n(n)
print(nth_fib)

print("--------------------------")


# O(2^n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
nth_fib = fibonacci(n)
print(nth_fib)