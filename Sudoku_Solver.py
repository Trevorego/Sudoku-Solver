def check_row(row, value):
    if value in row:
        return False
    return True

def check_column(sudoku, column, value):
    for i in sudoku:
        if i[column] == value:
            return False
    return True

def check_box(sudoku, i, j, value):
    if (i < 3):
        if (j < 3):
            for k in range(3):
                for t in range(3):
                    if (sudoku[k][t] == value):
                        return False
        elif (j < 6):
            for k in range(3):
                for t in range(3, 6):
                    if (sudoku[k][t] == value):
                        return False
        else:
            for k in range(3):
                for t in range(6, 9):
                    if (sudoku[k][t] == value):
                        return False
    elif (i < 6):
        if (j < 3):
            for k in range(3, 6):
                for t in range(3):
                    if (sudoku[k][t] == value):
                        return False
        elif (j < 6):
            for k in range(3, 6):
                for t in range(3, 6):
                    if (sudoku[k][t] == value):
                        return False
        else:
            for k in range(3, 6):
                for t in range(6, 9):
                    if (sudoku[k][t] == value):
                        return False
    else:
        if (j < 3):
            for k in range(6, 9):
                for t in range(3):
                    if (sudoku[k][t] == value):
                        return False
        elif (j < 6):
            for k in range(6, 9):
                for t in range(3, 6):
                    if (sudoku[k][t] == value):
                        return False
        else:
            for k in range(6, 9):
                for t in range(6, 9):
                    if (sudoku[k][t] == value):
                        return False
    return True


def main():
    sudoku = [
    [9, 0, 4, 0, 1, 5, 6, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 8, 0],
    [0, 0, 9, 0, 4, 2, 0, 0, 7],
    [0, 0, 0, 3, 0, 0, 2, 0, 0],
    [4, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 6],
    [1, 0, 0, 0, 2, 9, 5, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0]
    ]
    """[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]"""
    
    sudoku = solve(sudoku)
    if sudoku:
        for i in sudoku:
            print(i)
    else:
        print("It's unsolvable!!!")
        
def solved(sudoku):
    for i in sudoku:
        for j in i:
            if j == 0:
                return False
    return True

def solve(sudoku):
    if solved(sudoku):
        print("SOLVED!!!")
        return sudoku
    
    for i in sudoku:
        for j in range(len(i)):
            if (i[j] == 0):
                for x in range(1,10):
                    if check_column(sudoku, j, x) and check_row(i, x) and check_box(sudoku, sudoku.index(i), j, x):
                        i[j] = x
                        solvedOne = solve(sudoku.copy())
                        if solvedOne:
                            return solvedOne
                        i[j] = 0
                return
        
if __name__ == "__main__":
    main()