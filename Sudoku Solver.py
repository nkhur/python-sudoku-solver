class SudokuSolver:

    puzzle = [[0 for col in range(9)] for row in range(9)]

    def __init__(self, puzzle):
        self.puzzle = puzzle
    
    # find out if a guess is valid or not
    def valid_guess(self, row, col, guess):
        if guess not in range(1, 10): # numbers 1-9
            return False
        
        # check if valid in row
        row_values = self.puzzle[row]
        if guess in row_values:
            return False
        
        # check if valid in column
        col_values = [self.puzzle[i][col] for i in range(9)]
        if guess in col_values:
            return False
        
        # check if valid in its 9x9 box
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3
        for curr_row in range (box_start_row, box_start_row + 3):
            for curr_col in range (box_start_col, box_start_col + 3):
                if self.puzzle[curr_row][curr_col]==guess:
                    return False
                
        # all conditions satisfied
        return True

    # returns the row, col of the next empty box, else returns None
    def next_empty(self, start_row):
        for row in range(start_row, 9):
            for col in range(9):
                if self.puzzle[row][col]==0:
                    return row, col
        return None, None
        
    # solves the sudoku
    def solve_sudoku(self, start_row=0):
        row, col = self.next_empty(start_row)

        if row is None and col is None: # stopping case - sudoku complete!
            return True
        
        for guess in range(1, 10): # nums 1-9 will be tried
            if self.valid_guess(row, col, guess):
                self.puzzle[row][col] = guess
                isSolved = self.solve_sudoku(row)
                if isSolved:
                    return True
                else :
                    self.puzzle[row][col] = 0 # resetting the box
                    continue
            else: # the guess isn't valid
                if guess < 9 :
                    continue
                else :
                    return False

    # print the puzzle in a readable format
    def print_puzzle(self):
        for row in range(9):
            for col in range(9):
                print(self.puzzle[row][col], end=" ")
                if (col+1)%3 == 0:
                    print("| ", end="")
            if (row+1)%3==0:
                print("\n---------------------", end="")
            print()
        print("\n")


if __name__ == '__main__':
    # example sudoku
    sudoku = [
        [5, 3, 0,  0, 7, 0,  9, 0, 0],
        [6, 0, 0,  1, 9, 5,  0, 0, 0],
        [0, 9, 8,  0, 0, 0,  0, 6, 0],

        [8, 0, 0,  0, 6, 1,  0, 0, 3],
        [4, 0, 0,  0, 0, 3,  0, 0, 1],
        [7, 0, 0,  0, 2, 4,  0, 0, 6],

        [0, 6, 0,  0, 0, 0,  2, 8, 0],
        [0, 0, 0,  4, 1, 9,  0, 0, 5],
        [0, 0, 0,  0, 8, 0,  0, 7, 9]
    ]

    sudoku1 = SudokuSolver(sudoku)
    isSolved = sudoku1.solve_sudoku()
    if isSolved:
        sudoku1.print_puzzle()
    else :
        print("Can't be solved :(")
