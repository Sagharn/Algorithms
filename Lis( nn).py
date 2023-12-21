def longest_increasing_subarray(arr, n):
    LIS = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                LIS[i] = max(LIS[j] + 1, LIS[i])

    return LIS


def main():
    n = int(input("enter array length: "))
    print()

    array = []
    for i in range(n):
        array.append(int(input()))

    arr = longest_increasing_subarray(array, n)

    index_of_max = 0
    max_val = arr[0]
    for i in range(1, n):
        if max_val < arr[i]:
            max_val = arr[i]
            index_of_max = i

    print("lis length:", max_val)

    lis = []
    for i in range(index_of_max, -1, -1):
        if max_val == arr[i]:
            lis.append(array[i])
            max_val -= 1

    lis.reverse()
    print("Sub Array:")
    print(" ".join(map(str, lis)))


if __name__ == "__main__":
    main()
