# time complexity = O(sqrt(n))
def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)


n = int(input())
prime = is_prime(n)
print(prime)
