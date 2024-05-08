def add(matrix, row, col, value):
    try:
        row = int(row)
        col = int(col)
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            matrix[row][col] += int(value)
        else:
            return "Invalid coordinates"
    except ValueError:
        return "Invalid input values"

def subtract(matrix, row, col, value):
    try:
        row = int(row)
        col = int(col)
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            matrix[row][col] -= int(value)
        else:
            return "Invalid coordinates"
    except ValueError:
        return "Invalid input values"

rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]


line = input()

while line != "END":
    line = line.split()
    command = line[0]
    row = line[1]
    col = line[2]
    value = line[3]

    if command == "Add":
        result = add(matrix, row, col, value)
        if result:
            print(result)
    elif command == "Subtract":
        result = subtract(matrix, row, col, value)
        if result:
            print(result)

    line = input()

for row in matrix:
    print(" ".join(map(str, row)))