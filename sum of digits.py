# time complexity : O(log10(n))
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


total = int(input())
print(sum_of_digits(total))
