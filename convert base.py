# time complexity : O(log n)
def convert_base(n, b=2):
    if n < b:
        return str(n)
    else:
        return convert_base(n // b, b) + str(n % b)


n = int(input())
print(convert_base(n))
