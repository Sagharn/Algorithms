def tiling_divide_conquer(size, startx, starty, matrix):
    global tiling_count
    if size == 2:
        for i in range(size):
            for j in range(size):
                if matrix[i + startx][j + starty] == 0:
                    matrix[i + startx][j + starty] = tiling_count
        tiling_count += 1
        return matrix

    row, column = None, None
    for i in range(size):
        for j in range(size):
            if matrix[i + startx][j + starty] != 0:
                row = i + startx
                column = j + starty
                break

    print(f"Tail position is {row} {column}")

    if row < size / 2 + startx and column < size / 2 + starty:
        matrix[startx + size // 2][starty + size // 2] = tiling_count
        matrix[startx + size // 2][starty + size // 2 - 1] = tiling_count
        matrix[startx + size // 2 - 1][starty + size // 2] = tiling_count
        tiling_count += 1
    elif row >= size / 2 + startx and column < size / 2 + starty:
        matrix[startx + size // 2][starty + size // 2] = tiling_count
        matrix[startx + size // 2 - 1][starty + size // 2 - 1] = tiling_count
        matrix[startx + size // 2 - 1][starty + size // 2] = tiling_count
        tiling_count += 1
    elif row < size / 2 + startx and column >= size / 2 + starty:
        matrix[startx + size // 2 - 1][starty + size // 2 - 1] = tiling_count
        matrix[startx + size // 2][starty + size // 2 - 1] = tiling_count
        matrix[startx + size // 2][starty + size // 2] = tiling_count
        tiling_count += 1
    elif row >= size / 2 + startx and column >= size / 2 + starty:
        matrix[startx + size // 2 - 1][starty + size // 2 - 1] = tiling_count
        matrix[startx + size // 2][starty + size // 2 - 1] = tiling_count
        matrix[startx + size // 2 - 1][starty + size // 2] = tiling_count
        tiling_count += 1

    output(matrix)
    tiling_divide_conquer(size // 2, startx, starty + size // 2, matrix)
    tiling_divide_conquer(size // 2, startx, starty, matrix)
    tiling_divide_conquer(size // 2, startx + size // 2, starty, matrix)
    tiling_divide_conquer(size // 2, startx + size // 2, starty + size // 2, matrix)
    return matrix


def output(matrix):
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end="\t")
        print()
    print("-----------------------------------")


if __name__ == "__main__":
    size = int(input("Enter size of square: "))
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    row = int(input("Enter row for the point that you don't want to tile: "))
    column = int(input("Enter column for the point that you don't want to tile: "))

    if row < size and column < size:
        matrix[row][column] = -1
    else:
        print("Your point is out of matrix size.")
        exit(0)

    tiling_count = 1
    matrix = tiling_divide_conquer(size, 0, 0, matrix)

    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end="\t")
        print()
