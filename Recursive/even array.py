def even(arr):
    if not arr:
        return 0

    first_element = arr[0]
    array = arr[1:]
    x = even(array)

    return (first_element % 2 == 0) + x


input_array = list(map(int, input().split()))

even_count = even(input_array)

print(even_count)
