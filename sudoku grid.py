import tkinter as tk
from tkinter import messagebox

# Sudoku Solver Function
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False

    return True

def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entries[i][j].get()
            row.append(int(value) if value.isdigit() else 0)
        board.append(row)
    return board

def display_solution(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))

def solve_button_action():
    board = get_board()

    if solve_sudoku(board):
        display_solution(board)
        messagebox.showinfo("Success", "Sudoku solved successfully!")
    else:
        messagebox.showerror("Error", "No solution exists for the given Sudoku puzzle.")

def clear_grid():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

# Create GUI
root = tk.Tk()
root.title("Sudoku Solver")

frame = tk.Frame(root)
frame.pack(pady=10)

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Solve", command=solve_button_action).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Clear", command=clear_grid).grid(row=0, column=1, padx=10)

root.mainloop()
