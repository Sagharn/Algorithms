# time complexity : O(n)
def string_to_int(s):
    if not s:
        return 0
    if s[0] == '-':
        sign = -1
        s = s[1:]
    else:
        sign = 1
    return sign * (ord(s[-1]) - ord('0')) + 10 * string_to_int(s[:-1])


str_int = str(input())
print(string_to_int(str_int))
