# time complexity : O(n)
def find_max(array):
    if len(array) == 0:
        return None

    max_val = array[0]
    for item in array:
        if item > max_val:
            max_val = item

    return max_val


arr = [3, 7, 1, 9, 4, 5]
max_value = find_max(arr)
print(max_value)
