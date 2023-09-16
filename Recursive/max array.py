# time complexity : O(n)
def find_max(arr, index=0, max_value=float('-inf')):
    if index == len(arr):
        return max_value
    if arr[index] > max_value:
        max_value = arr[index]
    return find_max(arr, index + 1, max_value)


arr = [3, 7, 1, 9, 4, 5]
max_value = find_max(arr)
print(max_value)
