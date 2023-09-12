# time complexity = O(n)
def is_palindrome(n):
    n = n.lower().replace(" ", "")
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return is_palindrome(n[1:-1])


palindrome = str(input())
print(is_palindrome(palindrome))
