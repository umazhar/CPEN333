# student name: Umair Mazhar
# student number: 20333308

from concurrent.futures import process
from multiprocessing import Process

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 

        As usual, this function must not mutate puzzle 
    """
    values = set()
    for i in range(0, 9):
        values.add(puzzle[i][column])
    if (len(values) != 9):
        print("Column "+str(column)+" not valid")
    else:
        print("Column "+str(column)+" valid")


def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 

        As usual, this function must not mutate puzzle 
    """
    values = set()
    for i in range(0, 9):
        values.add(puzzle[row][i])
    if (len(values) != 9):
        print("Row "+str(row)+" not valid")
    else:
        print("Row "+str(row)+" valid")


def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list

        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 

        As usual, this function must not mutate puzzle 
    """
    values = set()

    #finding coordinate of first cell in each subgrid
    row_index = (subgrid//3)*3
    col_index = (subgrid%3)*3

    #adding all values in subgrid to set
    for i in range(row_index,row_index+3):
        for j in range(col_index, col_index+3):
            values.add(puzzle[i][j])
    
    #checking if set is correct size
    if (len(values) != 9):
        print("Subgrid "+str(subgrid)+" not valid")
    else:
        print("Subgrid "+str(subgrid)+" valid")
        
if __name__ == "__main__":
    test1 = [[6, 2, 4, 5, 3, 9, 1, 8, 7],
             [5, 1, 9, 7, 2, 8, 6, 3, 4],
             [8, 3, 7, 6, 1, 4, 2, 9, 5],
             [1, 4, 3, 8, 6, 5, 7, 2, 9],
             [9, 5, 8, 2, 4, 7, 3, 6, 1],
             [7, 6, 2, 3, 9, 1, 4, 5, 8],
             [3, 7, 1, 9, 5, 6, 8, 4, 2],
             [4, 9, 6, 1, 8, 2, 5, 7, 3],
             [2, 8, 5, 4, 7, 3, 9, 1, 6]
             ]
    test2 = [[6, 2, 4, 5, 3, 9, 1, 8, 7],
             [5, 1, 9, 7, 2, 8, 6, 3, 4],
             [8, 3, 7, 6, 1, 4, 2, 9, 5],
             [6, 2, 4, 5, 3, 9, 1, 8, 7],
             [5, 1, 9, 7, 2, 8, 6, 3, 4],
             [8, 3, 7, 6, 1, 4, 2, 9, 5],
             [6, 2, 4, 5, 3, 9, 1, 8, 7],
             [5, 1, 9, 7, 2, 8, 6, 3, 4],
             [8, 3, 7, 6, 1, 4, 2, 9, 5]
             ]
    test3 = [[6, 2, 4, 5, 3, 9, 1, 8, 7],
             [5, 1, 9, 7, 2, 8, 6, 3, 4],
             [8, 3, 7, 6, 1, 4, 2, 9, 5],
             [1, 4, 3, 6, 6, 5, 2, 2, 9],
             [9, 5, 8, 2, 4, 7, 3, 6, 1],
             [7, 6, 2, 3, 9, 1, 4, 5, 8],
             [3, 7, 1, 9, 5, 6, 8, 4, 2],
             [4, 9, 6, 1, 8, 2, 5, 7, 9],
             [2, 8, 5, 4, 7, 3, 9, 1, 6]
             ]

    testcase = test1  # modify here for other testcases
    SIZE = 9

    d={} #empty dictionary

    for x in range(0,9): #creating 9 of each process
        d[x] = Process(target = checkColumn, args = (testcase, x)) #creating multiple processes 
        d[x+9] = Process(target = checkRow, args = (testcase, x)) #creating multiple processes 
        d[x+18] = Process(target = checkSubgrid, args = (testcase, x)) #creating multiple processes 
      
    for x in range(0, 27):
        d[x].start()

    for x in range(0, 27):
        d[x].join()



    
