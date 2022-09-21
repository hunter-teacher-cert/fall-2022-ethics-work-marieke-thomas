# sudoku.py
# Marieke Thomas
# CSCI 77800 Fall 2022
# collaborators: Jeff Olsen
# consulted:https://www.websudoku.com/?select=1&level=3, puzzle # 4,575,577,303 (source of sudoku puzzles)

import puzzle_book
import random
puzzle = puzzle_book.flatten_puzzle(puzzle_book.evil_puzzle)
# Just change the name of the puzzle you want to solve at the end of line 3 to solve a different puzzle

class Board:
    def __init__(self):
        self.rows = []
        self.columns = []
        self.boxes = []

board = Board()        

for i in range(9):
    board.rows.append([])
    board.columns.append([])
    board.boxes.append([])


class Cell:
    def __init__(self,value,row,column):
        self.value = value
        self.row = row
        self.column = column
        self.allowed = [1,2,3,4,5,6,7,8,9]
        self.guess = False
        self.box = 9
        # The 9 is a placeholder value (the boxes only go up to 8). The next bit of code assigns the box number based on row and column.
        self.skip_guess = False
        self.abs_position = 100
        # also a placeholder for absolute position (number from 0 to 80)

# Make the cells and add them to the correct row/column/box lists. Also renumber the cell box properly.
# x and y are acting like (x,y) coordinates here (except y increases going down). Also, the boxes are numbered starting upper left, going across each row.
for y in range(9):
    for x in range(9):
        new_cell=Cell(0,y,x)
        board.rows[y].append(new_cell)
        board.columns[x].append(new_cell)
        if x < 3 and y < 3:
            board.boxes[0].append(new_cell)
            new_cell.box = 0
        elif x < 6 and y < 3:
            board.boxes[1].append(new_cell)
            new_cell.box = 1
        elif y < 3:
            board.boxes[2].append(new_cell)
            new_cell.box = 2
        elif x < 3 and y < 6:
            board.boxes[3].append(new_cell)
            new_cell.box = 3
        elif x < 6 and y < 6:
            board.boxes[4].append(new_cell)
            new_cell.box = 4
        elif y < 6:
            board.boxes[5].append(new_cell)
            new_cell.box = 5
        elif x < 3:
            board.boxes[6].append(new_cell)
            new_cell.box = 6
        elif x < 6:
            board.boxes[7].append(new_cell)
            new_cell.box = 7
        else:
            board.boxes[8].append(new_cell)
            new_cell.box = 8
        

# print(board.columns[0][8].box)
# print(board.boxes[4][2].row)
# print(board.boxes[4][2].column)


# Load the puzzle into the board
for i in range(81):
    row_number = int(i/9)
    column_number = i%9
    # box_number = int(column_number/3) + 3*int(row_number/3)
    # box_position = (i%3) + 3*(row_number%3)
    board.rows[row_number][column_number].value = puzzle[i]
    board.rows[row_number][column_number].abs_position = i
    # board.columns[column_number][row_number].value = puzzle[i]
    # board.boxes[box_number][box_position].value = puzzle[i]

# for i in range(9):
#     print(board.rows[8][i].value)


def check_answer():
    contradiction = False
    for row in board.rows:
        row_list = []
        for x in range(9):
            row_list.append(row[x].value)
        for y in range(1,10):
            if row_list.count(y) != 1:
                contradiction = True
    for row in board.columns:
        row_list = []
        for x in range(9):
            row_list.append(row[x].value)
        for y in range(1,10):
            if row_list.count(y) != 1:
                contradiction = True
    for row in board.boxes:
        row_list = []
        for x in range(9):
            row_list.append(row[x].value)
        for y in range(1,10):
            if row_list.count(y) != 1:
                contradiction = True
    if contradiction == False:
        return True
    else:
        return False


def print_board():
    board_list = []
    for row in board.rows:
        row_list = []
        for x in range(9):
            row_list.append(row[x].value)
        board_list.append(row_list)
    puzzle_book.print_puzzle(board_list)
    
# print_board()
# print(board.rows[1][0].value)
# print(board.columns[0][1].value)
# board.rows[1][0].value = 3
# print(board.rows[1][0].value)
# print(board.columns[0][1].value)

def check_cell(cell):
    if cell.value != 0:
        cell.allowed = [cell.value]
        return
    global has_anything_changed
    # check the row (Note: this checks itself too, but shouldn't be a problem since cell value is 0)
    for square in board.rows[cell.row]:
        if square.value in cell.allowed:
            cell.allowed.remove(square.value)
            has_anything_changed = True
    # check the column
    for square in board.columns[cell.column]:
        if square.value in cell.allowed:
            cell.allowed.remove(square.value)
            has_anything_changed = True
    # check the box
    for square in board.boxes[cell.box]:
        if square.value in cell.allowed:
            cell.allowed.remove(square.value)
            has_anything_changed = True
    # Assign the cell a value if possible
    if len(cell.allowed) == 1:
        cell.value = cell.allowed[0]
            
def check_by_row():
    global has_anything_changed
    current_group = 0
    for group in board.rows:
        for x in range(1,10):
            possible_cells = []
            for cell in group:
                if x in cell.allowed:
                    possible_cells.append(cell)
            if len(possible_cells) == 1 and possible_cells[0].value != x:
                possible_cells[0].value = x
                possible_cells[0].allowed = [x]
                has_anything_changed = True
            # if current_group == 3 and x == 6:
            #     for cell in possible_cells:
            #         print(cell.column)
            # print("x is currently "+ str(x) + ". And the row is currently row " + str(current_group))
            # print("there are this many allowed cells: " + str(len(possible_cells)))
            # print("The allowed values for the (4,1) square are: " + str(board.rows[4][1].allowed))
            if possible_cells[0].value != x:
                possible_boxes = []
                for cell in possible_cells:
                    possible_boxes.append(cell.box)
                    # Eliminate duplicates
                possible_boxes = list(dict.fromkeys(possible_boxes))
                if len(possible_boxes) == 1:
                    # We don't know which cell has number x, but we know it must be in a particular box, so we can remove x from other cells in the box
                    for cell in board.boxes[possible_boxes[0]]:
                        if cell.row != current_group:
                            if x in cell.allowed:
                                cell.allowed.remove(x)
                                has_anything_changed = True
        current_group += 1
                                    
def check_by_column():
    global has_anything_changed
    current_group = 0
    for group in board.columns:
        for x in range(1,10):
            possible_cells = []
            for cell in group:
                if x in cell.allowed:
                    possible_cells.append(cell)
            if len(possible_cells) == 1 and possible_cells[0].value != x:
                possible_cells[0].value = x
                possible_cells[0].allowed = [x]
                has_anything_changed = True
            # print("x is currently "+ str(x) + ". And the column is currently " + str(current_group))
            # print("there are this many allowed cells: " + str(len(possible_cells)))
            if possible_cells[0].value != x:
                possible_boxes = []
                for cell in possible_cells:
                    possible_boxes.append(cell.box)
                    # Eliminate duplicates
                    possible_boxes = list(dict.fromkeys(possible_boxes))
                if len(possible_boxes) == 1:
                    # We don't know which cell has number x, but we know it must be in a particular box, so we can remove x from other cells in the box
                    for cell in board.boxes[possible_boxes[0]]:
                        if cell.column != current_group:
                            if x in cell.allowed:
                                cell.allowed.remove(x)
                                has_anything_changed = True
        current_group += 1

def check_by_box():
    global has_anything_changed
    current_group = 0
    for group in board.boxes:
        for x in range(1,10):
            possible_cells = []
            for cell in group:
                if x in cell.allowed:
                    possible_cells.append(cell)
            if len(possible_cells) == 1 and possible_cells[0].value != x:
                possible_cells[0].value = x
                possible_cells[0].allowed = [x]
                has_anything_changed = True
            # if current_group == 3 and x == 6:
            #     for cell in possible_cells:
            #         print(cell.column)
            # print("x is currently "+ str(x) + ". And the row is currently row " + str(current_group))
            # print("there are this many allowed cells: " + str(len(possible_cells)))
            # print("The allowed values for the (4,1) square are: " + str(board.rows[4][1].allowed))
            if possible_cells[0].value != x:
                possible_rows = []
                possible_columns = []
                for cell in possible_cells:
                    possible_rows.append(cell.row)
                    possible_columns.append(cell.column)
                    # Eliminate duplicates
                possible_rows = list(dict.fromkeys(possible_rows))
                possible_columns = list(dict.fromkeys(possible_columns))
                if len(possible_rows) == 1:
                    # We don't know which cell has number x, but we know it must be in a particular row, so we can remove x from other cells in the row
                    for cell in board.rows[possible_rows[0]]:
                        if cell.box != current_group:
                            if x in cell.allowed:
                                cell.allowed.remove(x)
                                has_anything_changed = True
                if len(possible_columns) == 1:
                    for cell in board.columns[possible_columns[0]]:
                        if cell.box != current_group:
                            if x in cell.allowed:
                                cell.allowed.remove(x)
                                has_anything_changed = True
        current_group += 1

hypothetical_has_anything_changed = False
guess_failed = False
def hypothetical_check_cell(cell):
  # This is the similar to the check cell function above, but checks the hypothetical values rather than the known values (in order to guess and check to reach a solution)
    global hypothetical_has_anything_changed
    global guess_failed
    if cell.value != 0:
        return
    hypothetical_allowed = cell.allowed
    # check the row (Note: this checks itself too, but shouldn't be a problem since cell value is 0)
    for square in board.rows[cell.row]:
        if square.value in hypothetical_allowed:
            hypothetical_allowed.remove(square.value)
            hypothetical_has_anything_changed = True
    # check the column
    for square in board.columns[cell.column]:
        if square.value in cell.allowed:
            hypothetical_allowed.remove(square.value)
            hypothetical_has_anything_changed = True
    # check the box
    for square in board.boxes[cell.box]:
        if square.value in cell.allowed:
            hypothetical_allowed.remove(square.value)
            hypothetical_has_anything_changed = True
    # Assign the cell a value if possible
    if len(hypothetical_allowed) == 1:
        cell.value = hypothetical_allowed[0]
        cell.guess = True
    if len(hypothetical_allowed) == 0:
        guess_failed = True

def guess_and_check():
  # This function guesses a possible value for one of the boxes and checks if that solves the puzzle or creates a contradiction. If the guess creates a contradiction, then the guessed value is impossible and is eliminated from the possible values list. If the guess doesn't solve the puzzle and also doesn't yield a contradiction, the values are reverted back to their previous state.
  # print("making a guess")
    global hypothetical_has_anything_changed
    global guess_failed
    made_a_guess = False
    guess_failed = False
    guess_row = 9
    guess_column = 9
    # first round guess-- guess on a square that only has 2 possibilities
    for row in board.rows:
        for cell in row:
            # print("guessing cell " + str(cell.row) + "," + str(cell.column))
            if cell.value != 0:
                continue
            if len(cell.allowed)>2:
                continue
            if cell.skip_guess == True:
                continue
            cell.value = cell.allowed[0]
            cell.guess = True
            made_a_guess = True
            guess_row = cell.row
            guess_column = cell.column
            break
        if made_a_guess == True:
            break
    # second round guess-- if no squares have been narrowed down to 2, guess on any square
    if made_a_guess == False:
        for row in board.rows:
            for cell in row:
                if cell.value != 0:
                    continue
                cell.value = cell.allowed[0]
                cell.guess = True
                made_a_guess = True
                guess_row = cell.row
                guess_column = cell.column
                break
            if made_a_guess == True:
                break
    # Now solve out the puzzle (hypothetically) based on the guess
    hypothetical_has_anything_changed = True
    while hypothetical_has_anything_changed == True and guess_failed == False:
        hypothetical_has_anything_changed = False
        for row in board.rows:
            for cell in row:
                hypothetical_check_cell(cell)
         # Ideally there should be a hypothetical_check_row/column/box function here
    # Check if the solution works. If not, undo the changes.
    if check_answer():
        return
    else:
        for row in board.rows:
            for cell in row:
                if cell.guess:
                    cell.value = 0
                    cell.guess = False
        if guess_failed == True:
            # print("guess failed")
            board.rows[guess_row][guess_column].allowed.pop[0]
            if len(board.rows[guess_row][guess_column].allowed) == 1:
                board.rows[guess_row][guess_column].value = board.rows[guess_row][guess_column].allowed[0]
        else:
            # print("guess didn't fail, but also didn't solve the puzzle")
            board.rows[guess_row][guess_column].skip_guess = True
        return
        
def brute_force():
  # This function randomly tries a possible solution to the puzzle (consistent with known information up to this point) and checks if the puzzle is solved. If not, it reverses the guesses and guesses again until the solution is found.
    counter = 0
    while True:
        counter += 1
        for row in board.rows:
            for cell in row:
                if cell.value == 0:
                    random_choice = random.randrange(len(cell.allowed))
                    cell.value = cell.allowed[random_choice]
                    cell.guess = True
        if check_answer():
            print_board()
            break
        else:
            for row in board.rows:
                for cell in row:
                    if cell.guess == True:
                        cell.value = 0
                        cell.guess = False
    # print("Ran the brute force loop " + str(counter) + " times.")

    
# Actually solve the puzzle. The counter is to avoid crashing the program with an infinite while loop in case the puzzle is unsolveable.
counter = 0
while counter < 20:
    # print("Running the main loop")
    counter += 1
    has_anything_changed = False
    if check_answer():
        print_board()
        break
    for row in board.rows:
        for cell in row:
            check_cell(cell)
    check_by_row()
    check_by_column()
    check_by_box()
    if has_anything_changed == False:
        # print("Shit, this puzzle is hard. Time for guess and check")
        guess_and_check()
    # print(counter)
    # print_board()
    # print("\n")
    
if check_answer() == False:
    brute_force()

if check_answer() == False:
    print("This is a very hard puzzle.")