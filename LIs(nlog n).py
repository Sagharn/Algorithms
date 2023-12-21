def lis(arr):
    n = len(arr)
    lis_length = [1] * n
    prev_index = [-1] * n  # To store the index of the previous element in the LIS

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis_length[i] < lis_length[j] + 1:
                lis_length[i] = lis_length[j] + 1
                prev_index[i] = j

    max_lis_index = lis_length.index(max(lis_length))
    lis_elements = []

    # Reconstruct the LIS
    while max_lis_index != -1:
        lis_elements.append(arr[max_lis_index])
        max_lis_index = prev_index[max_lis_index]

    lis_elements.reverse()
    return lis_length[lis_length.index(max(lis_length))], lis_elements


user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Find and print the length and elements of LIS
length, elements = lis(numbers)
print(f"Length of Longest Increasing Subsequence: {length}")
print("Elements of Longest Increasing Subsequence:", elements)
