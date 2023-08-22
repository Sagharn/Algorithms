def even(array, index):
    if index >= len(array):
        return 0
    temp = 0
    if array[index] % 2 == 0:
        temp = 1
    return temp + even(array, index + 1)


arr = [6, 9, 8, 4, 1, 12]
print(even(arr, 0))
