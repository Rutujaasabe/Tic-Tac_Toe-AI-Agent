import tkinter as tk
from tkinter import messagebox

class TicTacToeAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        # Define colors and fonts
        self.bg_color = '#2E86AB'  # Change to your desired background color
        self.button_bg_color = '#F0F0F0'  # Change to your desired button background color
        self.button_fg_color = '#000000'  # Change to your desired button text color
        self.font = ('Arial', 30)

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text=' ', font=self.font, width=6, height=2,
                                              command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j].config(bg=self.button_bg_color, fg=self.button_fg_color)

        # Set window background color
        self.window.configure(bg=self.bg_color)

    def on_click(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'X':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state='disabled', disabledforeground=self.button_fg_color)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.current_player = 'O'
                self.ai_move()

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(row[col] == player for row in self.board):
                return True

        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O', state='disabled', disabledforeground=self.button_fg_color)
            if self.check_winner('O'):
                messagebox.showinfo("Game Over", "AI agent wins!!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.current_player = 'X'

    def minimax(self, board, depth, maximizing_player):
        if self.check_winner('O'):
            return 1
        if self.check_winner('X'):
            return -1
        if self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        eval = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        eval = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        min_eval = min(min_eval, eval)
            return min_eval

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeAI()
    game.run()
