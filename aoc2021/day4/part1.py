import re
from dataclasses import dataclass

@dataclass
class Cell:
    val: float
    checked: bool

numbers = []
boards = []
with open('input.txt', 'r', encoding='utf8') as f:
    line_number = 0
    board = []
    for line in f:
        if line == "\n":
            if board != []: 
                boards.append(board)
                board = []
            continue
        if line_number == 0:
            numbers = [int(n) for n in line.strip("\n").split(",")]
        else:
            board.append([Cell(int(n), False) for n in re.split("\s+", line.strip("\n").strip(" "))])

        line_number += 1
        
boards.append(board)    # Add last board

def check_finished(board):
    for row in board:
        row_complete = True
        for cell in row:
            row_complete &= cell.checked
        if row_complete:
            return True

    for i in range(len(board)):
        col_complete = True
        for cell in [row[i] for row in board]:
            col_complete &= cell.checked
        if col_complete:
            return True
    return False

def sum_of_uncalled(board):
    sum = 0
    for row in board:
        for cell in row:
            if not cell.checked:
                sum += cell.val
    return sum

winning_board = []
last_called = -1
for called_number in numbers:
    for board in boards:
        for row in board:
            for cell in row:
                if cell.val == called_number and not cell.checked:
                    cell.checked = True
        if check_finished(board):
            winning_board = board
            last_called = called_number
            break
    if last_called != -1:
        break


print(sum_of_uncalled(board) * last_called)
