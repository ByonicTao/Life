from time import sleep


size = 20

board = [[0 for j in range(size)] for i in range(size)]
copy = [[0 for j in range(size)] for i in range(size)]
board[5][5] = 1
board[5][6] = 1
board[6][5] = 1
board[4][5] = 1


def printBoard(table):
    for layer in range(len(table)):
        for spot in range(len(table[layer])):
            if table[layer][spot] == 0:
                print(" , ", end="")
            else:
                print("0, ", end="")
        print()
    print("--------------------------------------------")


def getNeighbours(row, column, table):
    result = 0
    if row == 0:
        if column == 0:
            result += table[row][column + 1] + table[row + 1][column] + table[row + 1][column + 1]
            return result
        elif column == len(table[0]) - 1:
            result += table[row][column - 1] + table[row + 1][column] + table[row + 1][column - 1]
            return result
        else:
            result += table[row][column - 1] + table[row][column + 1]
            result += table[row + 1][column - 1] + table[row + 1][column] + table[row + 1][column - 1]
            return result
    elif row == len(table) - 1:
        if column == 0:
            result += table[row][column + 1] + table[row - 1][column] + table[row - 1][column + 1]
            return result
        elif column == len(table[0]) - 1:
            result += table[row][column - 1] + table[row - 1][column] + table[row - 1][column - 1]
            return result
        else:
            result += table[row][column - 1] + table[row][column + 1]
            result += table[row - 1][column - 1] + table[row - 1][column] + table[row - 1][column - 1]
            return result
    elif column == 0:
        result += table[row - 1][column] + table[row - 1][column + 1]
        result += table[row][column + 1]
        result += table[row + 1][column] + table[row + 1][column + 1]
        return result
    elif column == len(table[0]) - 1:
        result += table[row - 1][column] + table[row - 1][column - 1]
        result += table[row][column - 1]
        result += table[row + 1][column] + table[row + 1][column - 1]
        return result
    else:
        result += table[row - 1][column + 1] + table[row - 1][column] + table[row - 1][column - 1]
        result += table[row][column + 1] + table[row][column - 1]
        result += table[row + 1][column + 1] + table[row + 1][column] + table[row + 1][column - 1]
        return result


input()
printBoard(board)
while True:
    for a in range(len(board)):
        for b in range(len(board[a])):
            copy[a][b] = getNeighbours(a, b, board)

    for a in range(len(board)):
        for b in range(len(board[a])):
            if board[a][b] == 1:
                if copy[a][b] < 2 or copy[a][b] > 3:
                    board[a][b] = 0
            elif board[a][b] == 0:
                if copy[a][b] == 3:
                    board[a][b] = 1
    printBoard(board)
    sleep(1)
